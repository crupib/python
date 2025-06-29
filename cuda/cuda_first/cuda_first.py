import numpy as np
import pycuda.driver as cuda
import pycuda.autoinit
from pycuda.compiler import SourceModule
import warnings
warnings.filterwarnings("ignore", category=UserWarning)
kernel_code = """
__global__ void add(int *d_array, int N) {
    int idx = threadIdx.x + blockIdx.x * blockDim.x;
    if (idx < N) {
        d_array[idx] +=1 ;
    }
}
"""
mod = SourceModule(kernel_code,options=["--std=c++14", "-w"])
add = mod.get_function("add")

def initialize_data(N):
    h_array = np.arange(N).astype(np.int32)
    return h_array

def allocate_and_transfer(h_array):
    d_array = cuda.mem_alloc(h_array.nbytes)
    cuda.memcpy_htod(d_array, h_array)
    return d_array

def execute_kernel(d_array, N):
    block_dim = 256
    grid_dim = (N + block_dim - 1) // block_dim
    add(d_array, np.int32(N), block=(block_dim, 1, 1),grid=(grid_dim, 1))

def retrieve_and_cleanup(d_array, N):
    h_result = np.empty(N, dtype=np.int32)
    cuda.memcpy_dtoh(h_result, d_array)
    d_array.free()
    return h_result

def main():
    N = 1024
    h_array = initialize_data(N)
    d_array = allocate_and_transfer(h_array)
    execute_kernel(d_array, N)
    h_result = retrieve_and_cleanup(d_array, N)
    print("Original array: ", h_array)
    print("Result array: ", h_result)

if __name__ == "__main__":
    main()
