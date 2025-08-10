import os
os.add_dll_directory(r"C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\bin")
from idlelib.browser import transform_children

import pycuda.autoinit
import pycuda.driver as cuda
from pycuda.compiler import SourceModule
import numpy as np

module = SourceModule("""
__global__ void sum_reduce(float *g_idata, float *g_odata, unsigned n) {
    extern __shared__ float shared_data[];
    unsigned int tid = threadIdx.x;
    unsigned int i = blockIdx.x * blockDim.x + threadIdx.x;
    shared_data[tid] = (i < n) ?  g_idata[i] : 0;
    for (unsigned int s = 1; s < blockDim.x; s *=2) {
        if (tid % (2*s) == 0 ) {
           shared_data[tid] += shared_data[tid+s];
        }
        __syncthreads();
    }
    if (tid == 0) g_odata[blockIdx.x] = shared_data[0];
}
__global__ void max_reduce(float *g_idata, float *g_odata, unsigned n) {
    extern __shared__ float shared_data[];
    unsigned int tid = threadIdx.x;
    unsigned int i = blockIdx.x * blockDim.x + threadIdx.x;
    shared_data[tid] = (i < n) ?  g_idata[i] : -3.402823466e+38f ;
    __syncthreads();
    for (unsigned int s = 1; s < blockDim.x; s *=2) {
        if (tid % (2*s) == 0 ) {
           shared_data[tid] += fmaxf(shared_data[tid], shared_data[tid+s]);
        }
        __syncthreads();
    }
    if (tid == 0) g_odata[blockIdx.x] = shared_data[0];
}
""")
sum_reduce = module.get_function("sum_reduce")
max_reduce = module.get_function("max_reduce")

def parallel_sum(input_vector):
    n = len(input_vector)
    block_size = 512
    grid_size =(n+block_size-1)
    output_size = grid_size
    input_gpu = cuda.mem_alloc(input_vector.nbytes)
    output_gpu = cuda.mem_alloc(output_size*input_vector.dtype.itemsize )
    cuda.memcpy_htod(input_gpu, input_vector)
    sum_reduce(input_gpu, output_gpu, np.uint32(n), block=(block_size,1,1),
               grid=(grid_size,1),
               shared=block_size*input_vector.itemsize)
    output_vector = np.empty(output_size, dtype=np.float32)
    cuda.memcpy_dtoh(output_vector, output_gpu)
    total_sum = sum(output_vector)
    return total_sum
def parallel_max(input_vector):
    n = len(input_vector)
    block_size = 512
    grid_size =(n+block_size-1)
    output_size = grid_size
    input_gpu = cuda.mem_alloc(input_vector.nbytes)
    output_gpu = cuda.mem_alloc(output_size*input_vector.dtype.itemsize )
    cuda.memcpy_htod(input_gpu, input_vector)
    max_reduce(input_gpu, output_gpu, np.uint32(n), block=(block_size,1,1),
               grid=(grid_size,1),
               shared=block_size*input_vector.itemsize)
    output_vector = np.empty(output_size, dtype=np.float32)
    cuda.memcpy_dtoh(output_vector, output_gpu)
    global_max = max(output_vector)
    return global_max

vector = np.random.rand(1024).astype(np.float32)
sum_result = parallel_sum(vector)
max_result = parallel_max(vector)
print(sum_result)
print(max_result)
