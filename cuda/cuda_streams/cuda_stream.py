import numpy as np
import pycuda.driver as cuda
import pycuda.autoinit
from pycuda.compiler import SourceModule

# CUDA Kernel Code
mod = SourceModule("""
__global__ void matAddKernel(float *A, float *B, float *C, int width) {
    int idx = blockIdx.x * blockDim.x + threadIdx.x;
    if (idx < width) {
        C[idx] = A[idx] + B[idx];
    }
}
""", options=["-arch=sm_75", "--std=c++14"])

def execute_cuda_streams(A, B, width):
    A = A.astype(np.float32)
    B = B.astype(np.float32)

    A_gpu = cuda.mem_alloc(A.nbytes)
    B_gpu = cuda.mem_alloc(B.nbytes)
    C_gpu = cuda.mem_alloc(A.nbytes)

    stream1 = cuda.Stream()
    stream2 = cuda.Stream()

    cuda.memcpy_htod_async(A_gpu, A, stream=stream1)
    cuda.memcpy_htod_async(B_gpu, B, stream=stream2)

    mat_add = mod.get_function("matAddKernel")
    mat_add(A_gpu, B_gpu, C_gpu, np.int32(width), block=(256, 1, 1),
            grid=(int((width + 255) // 256), 1), stream=stream1)

    C = np.empty_like(A)
    cuda.memcpy_dtoh_async(C, C_gpu, stream=stream2)

    stream1.synchronize()
    stream2.synchronize()

    A_gpu.free()
    B_gpu.free()
    C_gpu.free()

    return C

if __name__ == "__main__":
    width = 1024

    # Generate random input data
    A = np.random.randn(width).astype(np.float32)
    B = np.random.randn(width).astype(np.float32)

    print("Input Matrix A (first 10 elements):")
    print(A[:10])

    print("Input Matrix B (first 10 elements):")
    print(B[:10])

    # Perform CUDA computation
    C = execute_cuda_streams(A, B, width)

    print("Resultant Matrix C (first 10 elements):")
    print(C[:10])
