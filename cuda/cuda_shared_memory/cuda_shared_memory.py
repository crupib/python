import pycuda.autoinit
import pycuda.driver as cuda
import numpy as np
from pycuda.compiler import SourceModule
import warnings
warnings.filterwarnings("ignore", category=UserWarning)
#Kernel code for matrix multiplication with shared memory tiling
kernel_code = """  __global__ void matrixMulShared(float *A, float *B, float *C, int N)
 {  
  __shared__ float tile_A[BLOCK_SIZE][BLOCK_SIZE];
  __shared__ float tile_B[BLOCK_SIZE][BLOCK_SIZE];
    int row = blockIdx.y * BLOCK_SIZE + threadIdx.y;
    int col = blockIdx.x * BLOCK_SIZE + threadIdx.x;
    float value = 0;
    for (int k = 0; k < gridDim.x; ++k){ 
      tile_A[threadIdx.y][threadIdx.x] = A[row * N + k * BLOCK_SIZE + threadIdx.x];
      tile_B[threadIdx.y][threadIdx.x] = B[(k * BLOCK_SIZE + threadIdx.y) * N + col];
      __syncthreads();
      for (int n = 0; n < BLOCK_SIZE; ++n)
        value += tile_A[threadIdx.y][n] *  tile_B[n][threadIdx.x];
      __syncthreads();
    } 
    C[row * N + col] = value;
}
"""
BLOCK_SIZE = 16
def initialize(N):
    A = np.random.rand(N, N).astype(np.float32)
    B = np.random.rand(N, N).astype(np.float32)
    C = np.zeros((N, N), dtype=np.float32)
    return A, B, C

N = 256
A, B, C = initialize(N)
A_gpu = cuda.mem_alloc(A.nbytes)
B_gpu = cuda.mem_alloc(B.nbytes)
C_gpu = cuda.mem_alloc(C.nbytes)

cuda.memcpy_htod(A_gpu, A)
cuda.memcpy_htod(B_gpu, B)
mod = SourceModule(kernel_code.replace("BLOCK_SIZE", str(BLOCK_SIZE)))
matrixMulShared = mod.get_function("matrixMulShared")
block = (BLOCK_SIZE, BLOCK_SIZE, 1)
grid = (N // BLOCK_SIZE, N // BLOCK_SIZE)
matrixMulShared(A_gpu, B_gpu, C_gpu, np.int32(N), block=block, grid=grid)
cuda.memcpy_dtoh(C, C_gpu)
print("Matrix C (Product of A and B):")
print(C)
A_gpu.free()
B_gpu.free()
C_gpu.free()
