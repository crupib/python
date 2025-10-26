import ctypes
import os
import sys

# --- Windows DLL loading (no-op on other OS) ---
if sys.platform == "win32":
    # Adjust the paths below if your CUDA install is in a different location
    os.add_dll_directory(r"C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v13.0\bin\x64")
    os.add_dll_directory(r"C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v13.0\lib\x64")
    # Optional: test DLL loading (will raise if missing)
    ctypes.WinDLL(r"C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v13.0\bin\x64\cudart64_13.dll")
    print("CUDA DLL loaded successfully!")

import numpy as np
import pycuda.driver as cuda
import pycuda.autoinit                    # creates a context for us
from pycuda.compiler import SourceModule

cuda_source = """
__global__ void add(int *a, int *b, int *c, int N)
{
  int idx = blockIdx.x * blockDim.x + threadIdx.x;
  if (idx < N) {
    c[idx] = a[idx] + b[idx];
  }
}
"""
mod = SourceModule(cuda_source)
add_kernel = mod.get_function("add")


def check_cuda_errors():
    """
    Robust CUDA error check across PyCUDA versions:
      1) If pycuda.driver.get_last_error exists, call it.
      2) If Context.get_last_error exists, call it.
      3) Otherwise, call Context.synchronize() which will raise if the device reported an error.
    If an error is detected, raise RuntimeError with a readable message when possible.
    """
    print("Checking CUDA errors")
    ctx = cuda.Context.get_current()

    # 1) module-level helper (preferred if available)
    get_last_err_fn = getattr(cuda, "get_last_error", None)
    if callable(get_last_err_fn):
        try:
            err = get_last_err_fn()
        except Exception as e:
            # If calling it fails, fall back to synchronize below
            err = None
        else:
            if err is not None and err != 0:
                # try to get a readable message
                msg = None
                try:
                    msg = cuda.get_error_string(err)
                except Exception:
                    msg = f"CUDA error code {err}"
                raise RuntimeError("CUDA Error: " + str(msg))
            return  # success, no error

    # 2) class-level Context.get_last_error (some versions expose this)
    cls_get_last = getattr(cuda.Context, "get_last_error", None)
    if callable(cls_get_last):
        try:
            err = cls_get_last()
        except Exception:
            err = None
        else:
            if err is not None and err != 0:
                try:
                    msg = cuda.get_error_string(err)
                except Exception:
                    msg = f"CUDA error code {err}"
                raise RuntimeError("CUDA Error: " + str(msg))
            return

    # 3) final fallback -- synchronize the context (raises on many kinds of device errors)
    try:
        ctx.synchronize()
    except Exception as e:
        # Wrap and re-raise with helpful context
        raise RuntimeError("CUDA sync failed (fallback check) — device reported error: " + str(e)) from e

    # If we reach here, we couldn't query a last-error value but synchronize succeeded;
    # assume no error (best-effort).
    return


def example_cuda_operation():
    N = 512
    a = np.random.randint(0, 10, size=N).astype(np.int32)
    b = np.random.randint(0, 10, size=N).astype(np.int32)
    c = np.zeros_like(a)

    a_gpu = b_gpu = c_gpu = None
    try:
        # allocate device memory and copy inputs
        a_gpu = cuda.mem_alloc(a.nbytes)
        b_gpu = cuda.mem_alloc(b.nbytes)
        c_gpu = cuda.mem_alloc(c.nbytes)
        cuda.memcpy_htod(a_gpu, a)
        cuda.memcpy_htod(b_gpu, b)

        # launch kernel
        block_size = 256
        grid_size = (N + block_size - 1) // block_size
        add_kernel(a_gpu, b_gpu, c_gpu, np.int32(N),
                   block=(block_size, 1, 1), grid=(grid_size, 1, 1))

        # ensure kernel finished (and detect errors)
        check_cuda_errors()

        # copy result back
        cuda.memcpy_dtoh(c, c_gpu)

        # final sync and error check
        check_cuda_errors()

    finally:
        # free device memory if it was allocated
        for ptr in (a_gpu, b_gpu, c_gpu):
            try:
                if ptr is not None:
                    ptr.free()
            except Exception:
                # ignore free errors but print them for debugging
                print("Warning: failed to free device memory:", sys.exc_info()[1])

    return a, b, c


if __name__ == "__main__":
    a, b, c = example_cuda_operation()
    print("Array A:", a[:10])
    print("Array B:", b[:10])
    print("Array C (Result):", c[:10])
