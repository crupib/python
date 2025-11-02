# corrected_shared_memory_matmul.py
import ctypes
import os
import sys

# --- Windows DLL loading (no-op on other OS) ---
if sys.platform == "win32":
    # Adjust these paths if your CUDA install is elsewhere
    os.add_dll_directory(r"C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v13.0\bin\x64")
    os.add_dll_directory(r"C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v13.0\lib\x64")
    # Optional: test DLL loading (will raise if missing)
    ctypes.WinDLL(r"C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v13.0\bin\x64\cudart64_13.dll")
    print("CUDA DLL loaded successfully!")

import numpy as np
import pycuda.autoinit                 # <-- auto init + make context
import pycuda.driver as cuda
from pycuda.compiler import SourceModule

# corrected kernel (note the B indexing fix using (row*N + col) math)
kernel_code = """
__global__ void matrixMulShared(float *A, float *B, float *C, int N)
{
  __shared__ float tile_A[BLOCK_SIZE][BLOCK_SIZE];
  __shared__ float tile_B[BLOCK_SIZE][BLOCK_SIZE];

  int row = blockIdx.y * BLOCK_SIZE + threadIdx.y;
  int col = blockIdx.x * BLOCK_SIZE + threadIdx.x;
  float value = 0.0f;

  // number of phases = number of tiles in a row = gridDim.x
  for (int k = 0; k < gridDim.x; k++) {
    // load tile of A and B into shared memory
    int aRow = row;
    int aCol = k * BLOCK_SIZE + threadIdx.x;
    int bRow = k * BLOCK_SIZE + threadIdx.y;
    int bCol = col;

    // bounds check (in case N not divisible by BLOCK_SIZE) - safe guard
    if (aRow < N && aCol < N)
      tile_A[threadIdx.y][threadIdx.x] = A[aRow * N + aCol];
    else
      tile_A[threadIdx.y][threadIdx.x] = 0.0f;

    if (bRow < N && bCol < N)
      tile_B[threadIdx.y][threadIdx.x] = B[bRow * N + bCol];
    else
      tile_B[threadIdx.y][threadIdx.x] = 0.0f;

    __syncthreads();

    for (int n = 0; n < BLOCK_SIZE; n++)
      value += tile_A[threadIdx.y][n] * tile_B[n][threadIdx.x];

    __syncthreads();
  }

  if (row < N && col < N)
    C[row * N + col] = value;
}
"""

BLOCK_SIZE = 16

def initialize(N):
    A = np.random.randn(N, N).astype(np.float32)
    B = np.random.randn(N, N).astype(np.float32)
    C = np.zeros((N, N), dtype=np.float32)
    return A, B, C

N = 256
A, B, C = initialize(N)

# allocate GPU buffers (autoinit created the context)
A_gpu = cuda.mem_alloc(A.nbytes)
B_gpu = cuda.mem_alloc(B.nbytes)      # <-- fixed typo here
C_gpu = cuda.mem_alloc(C.nbytes)

cuda.memcpy_htod(A_gpu, A)
cuda.memcpy_htod(B_gpu, B)

mod = SourceModule(kernel_code.replace("BLOCK_SIZE", str(BLOCK_SIZE)))
matrixMulShared = mod.get_function("matrixMulShared")

block = (BLOCK_SIZE, BLOCK_SIZE, 1)
grid = (int(np.ceil(N / BLOCK_SIZE)), int(np.ceil(N / BLOCK_SIZE)))

matrixMulShared(A_gpu, B_gpu, C_gpu, np.int32(N), block=block, grid=grid)

cuda.memcpy_dtoh(C, C_gpu)

print("Matrix C (A x B) sample entries:")
print(C[:4, :4])   # show a small sample

# free GPU memory
A_gpu.free()
B_gpu.free()
C_gpu.free()
# pycuda.autoinit will automatically clean up the context on program exit
