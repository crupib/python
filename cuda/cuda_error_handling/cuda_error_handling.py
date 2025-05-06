import pycuda.driver as cuda
import pycuda.autoinit
import numpy as np
from pycuda.compiler import SourceModule

# CUDA kernel
cuda_source = """
__global__ void add(int *a, int *b, int *c, int N)
{
    int index = threadIdx.x + blockIdx.x * blockDim.x;
    if (index < N) {  // Correct bounds check
        c[index] = a[index] + b[index];  // Write result to the correct index
    }
}
"""
mod = SourceModule(cuda_source, options=["-arch=sm_75", "--std=c++14"])
add = mod.get_function("add")

def example_cuda_operation():
    N = 512

    # Host arrays
    a = np.random.randint(0, 10, size=N).astype(np.int32)
    b = np.random.randint(0, 10, size=N).astype(np.int32)
    c = np.zeros_like(a)

    # Allocate device memory
    a_gpu = cuda.mem_alloc(a.nbytes)
    b_gpu = cuda.mem_alloc(b.nbytes)
    c_gpu = cuda.mem_alloc(c.nbytes)

    try:
        # Copy host data to device
        cuda.memcpy_htod(a_gpu, a)
        cuda.memcpy_htod(b_gpu, b)

        # Kernel configuration
        block_size = 256
        grid_size = (N + block_size - 1) // block_size

        # Launch kernel
        add(a_gpu, b_gpu, c_gpu, np.int32(N), block=(block_size, 1, 1), grid=(grid_size, 1))
        cuda.Context.synchronize()  # Ensure all CUDA operations are complete

        # Copy result back to host
        cuda.memcpy_dtoh(c, c_gpu)

    finally:
        # Cleanup device memory
        a_gpu.free()
        b_gpu.free()
        c_gpu.free()

    return a, b, c

# Run the example
try:
    a, b, c = example_cuda_operation()

    # Display results
    print("Array A: ", a)
    print("Array B: ", b)
    print("Array C (Result): ", c)

except cuda.Error as e:
    print(f"CUDA Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
