import ctypes
import os
# Add the correct directories
os.add_dll_directory(r"C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v13.0\bin\x64")
os.add_dll_directory(r"C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v13.0\lib\x64")

# Optional: test DLL loading
ctypes.WinDLL(r"C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v13.0\bin\x64\cudart64_13.dll")
print("CUDA DLL loaded successfully!")

import numpy as np
import pycuda.driver as cuda
import pycuda.autoinit                    # creates a context for us
from pycuda.compiler import SourceModule


mod = SourceModule("""
__global__ void matAddKernel(float *A, float *B, float *C, int width) 
{
  int idx = threadIdx.x + blockIdx.x * blockDim.x;
  if (idx < width) {
    C[idx] = A[idx] + B[idx];
  }
}
""")

def execute_cuda_streams(A, B, width):
    # ensure correct dtype
    A = A.astype(np.float32)
    B = B.astype(np.float32)

    # create two streams
    stream1 = cuda.Stream()
    stream2 = cuda.Stream()

    # allocate device memory
    A_gpu = cuda.mem_alloc(A.nbytes)
    B_gpu = cuda.mem_alloc(B.nbytes)
    C_gpu = cuda.mem_alloc(A.nbytes)

    # create pinned (page-locked) host buffers for async transfers
    h_a = cuda.pagelocked_empty_like(A)
    h_b = cuda.pagelocked_empty_like(B)
    h_out = cuda.pagelocked_empty_like(A)

    # copy input data into pinned buffers
    h_a[:] = A
    h_b[:] = B

    # async host -> device copies (one per stream as an example)
    cuda.memcpy_htod_async(A_gpu, h_a, stream=stream1)
    cuda.memcpy_htod_async(B_gpu, h_b, stream=stream2)

    # prepare and launch kernel into stream1 (for example)
    mat_add = mod.get_function("matAddKernel")
    block_size = 256
    grid_x = (int(width) + block_size - 1) // block_size

    mat_add(A_gpu, B_gpu, C_gpu, np.int32(width),
            block=(block_size, 1, 1),
            grid=(grid_x, 1, 1),
            stream=stream1)

    # async device -> host copy of result using stream2 (could be same stream1)
    cuda.memcpy_dtoh_async(h_out, C_gpu, stream=stream2)

    # wait for both streams to finish
    stream1.synchronize()
    stream2.synchronize()

    # copy result into a normal numpy array to return (or return h_out directly)
    C = np.empty_like(A)
    C[:] = h_out

    # free device memory
    A_gpu.free()
    B_gpu.free()
    C_gpu.free()

    return C

if __name__ == "__main__":
    width = 1024
    A = np.random.rand(width).astype(np.float32)
    B = np.random.rand(width).astype(np.float32)
    C = execute_cuda_streams(A, B, width)
    print("A array :")
    print(A[:10])
    print("B array :")
    print(B[:10])
    print("Resultant array C (first 10):")
    print(C[:10])
    # quick verify
    print("Max error:", np.max(np.abs(C - (A + B))))
