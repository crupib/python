import pycuda.driver as cuda
import pycuda.autoinit
from pycuda.compiler import SourceModule
import numpy as np

# CUDA kernel code
kernel_code = """
__global__ void add(int *a, int *b, int *c) {
    int idx = threadIdx.x + blockIdx.x * blockDim.x;
    c[idx] = a[idx] + b[idx];
}
"""

# Compile the kernel
mod = SourceModule(kernel_code, options=["-arch=sm_75", "--std=c++14"])

add = mod.get_function("add")

# Prepare data
a = np.array([1, 2, 3, 4], dtype=np.int32)
b = np.array([5, 6, 7, 8], dtype=np.int32)
c = np.empty_like(a)

# Allocate GPU memory
a_gpu = cuda.mem_alloc(a.nbytes)
b_gpu = cuda.mem_alloc(b.nbytes)
c_gpu = cuda.mem_alloc(c.nbytes)

# Copy data to GPU
cuda.memcpy_htod(a_gpu, a)
cuda.memcpy_htod(b_gpu, b)

# Launch kernel
block_size = 4
grid_size = 1
add(a_gpu, b_gpu, c_gpu, block=(block_size, 1, 1), grid=(grid_size, 1))

# Copy result back to CPU
cuda.memcpy_dtoh(c, c_gpu)

# Print the result
print("Result:", c)
