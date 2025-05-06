import pycuda.autoinit
import pycuda.driver as cuda
from pycuda.compiler import SourceModule
import numpy as np
import gc  # Garbage collector module

# CUDA kernel code
kernel_code = """
__global__ void addVectors(float *a, float *b, float *c, int n) {
    int tid = blockIdx.x * blockDim.x + threadIdx.x;
    if (tid < n) {
        c[tid] = a[tid] + b[tid];
    }
}
"""
def clear_cuda_cache():
    global mod
    mod = None  # Delete the SourceModule
    gc.collect()  # Run garbage collection
    cuda.Context.synchronize()  # Optional: Synchronize the context
n = 256
a = np.random.randn(n).astype(np.float32)
b = np.random.randn(n).astype(np.float32)
c = np.zeros(n, dtype=np.float32)

a_gpu = cuda.mem_alloc(a.nbytes)
b_gpu = cuda.mem_alloc(b.nbytes)
c_gpu = cuda.mem_alloc(c.nbytes)

cuda.memcpy_htod(a_gpu, a)
cuda.memcpy_htod(b_gpu, b)
mod = SourceModule(kernel_code, options=["--std=c++14"])
addVectors = mod.get_function("addVectors")
block_size = 128
grid_size = (n + block_size -1) // block_size

addVectors(a_gpu, b_gpu, c_gpu, np.int32(n), block=(block_size, 1, 1), grid=(grid_size,1))
c = np.empty_like(a)
cuda.memcpy_dtoh(c, c_gpu)
if np.allclose(c, a+b):
    print("OK")
else:
    print("FAIL")

# Clear CUDA Cache



clear_cuda_cache()
