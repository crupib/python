import numpy as np
import pycuda.driver as drv
import pycuda.autoinit
from pycuda.compiler import SourceModule

# CUDA Kernel Code
kernel_code = """
__global__ void incrementArray(float *arr, int N, float v) {
    int idx = blockIdx.x * blockDim.x + threadIdx.x;
    if (idx < N) {
        atomicAdd(&arr[idx], v);
    }
}

__global__ void parallelReduction(float *g_idata, float *g_odata, unsigned int n)
{
    extern __shared__ float sdata[];
    unsigned int tid = threadIdx.x;
    unsigned int i = blockIdx.x * (blockDim.x * 2) + threadIdx.x;

    // Load elements into shared memory
    sdata[tid] = (i < n) ? g_idata[i] + g_idata[i + blockDim.x] : 0;
    __syncthreads();

    // Perform parallel reduction
    for (unsigned int s = blockDim.x / 2; s > 0; s >>= 1) {
        if (tid < s) {
            sdata[tid] += sdata[tid + s];
        }
        __syncthreads();
    }

    // Write the result for this block to global memory
    if (tid == 0) g_odata[blockIdx.x] = sdata[0];
}
"""

# Compile CUDA kernel
mod = SourceModule(kernel_code, options=["--std=c++14"])
increment = mod.get_function("incrementArray")
parallel_reduction = mod.get_function("parallelReduction")

# Input data
N = 1024
x = np.random.randn(N).astype(np.float32)  # Random float array
v = 1.0  # Value to add

# Allocate device memory
x_gpu = drv.mem_alloc(x.nbytes)
drv.memcpy_htod(x_gpu, x)

# Kernel execution configuration
block_size = 256
grid_size = (N + block_size - 1) // block_size

# Call incrementArray kernel
increment(x_gpu, np.int32(N), np.float32(v), block=(block_size, 1, 1), grid=(grid_size, 1))

# Verify increment kernel
drv.memcpy_dtoh(x, x_gpu)
print("First 10 elements after increment:", x[:10])

# Set up for parallel reduction
sdata = np.zeros(grid_size).astype(np.float32)
sdata_gpu = drv.mem_alloc(sdata.nbytes)

# Call parallelReduction kernel
parallel_reduction(
    x_gpu, sdata_gpu, np.uint32(N),
    block=(block_size, 1, 1),
    grid=(grid_size, 1),
    shared=block_size * np.float32().nbytes
)

# Copy reduction result back to host
drv.memcpy_dtoh(sdata, sdata_gpu)

# Sum up results from the grid
result = np.sum(sdata)
print("Sum after parallel reduction (GPU):", result)

# Validate against numpy sum
expected_sum = np.sum(x)
print("Expected sum (CPU):", expected_sum)

# Check for correctness
if np.isclose(result, expected_sum):
    print("Test passed: Results match!")
else:
    print("Test failed: Results do not match.")
