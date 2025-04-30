import pycuda.driver as cuda
import pycuda.autoinit
import numpy as np
from pycuda.compiler import SourceModule
import os

def check_cuda_devices():
    cuda.init()
    print(f"Detected {cuda.Device.count()} CUDA devices")
    for i in range(cuda.Device.count()):
        dev = cuda.Device(i)
        print(f"[Device {i}] {dev.name()}, {dev.compute_capability()}, {dev.total_memory()/1024**2} MB")

kernel_code = """
__global__ void verify_installation(float *a, float *b, float *c, int N) {
    int idx = threadIdx.x + blockIdx.x * blockDim.x;
    if (idx < N) {
        c[idx] = a[idx] + b[idx];
    }
}
"""

def verify_cuda_installation():
    N = 1024
    a = np.random.random(N).astype(np.float32)
    b = np.random.random(N).astype(np.float32)
    c = np.zeros(N, dtype=np.float32)

    # Allocate GPU memory
    a_gpu = cuda.mem_alloc(a.nbytes)
    b_gpu = cuda.mem_alloc(b.nbytes)
    c_gpu = cuda.mem_alloc(c.nbytes)

    # Copy data to GPU
    cuda.memcpy_htod(a_gpu, a)
    cuda.memcpy_htod(b_gpu, b)

    # Compile and launch kernel
    mod = SourceModule(kernel_code, options=["--std=c++14"])
    func = mod.get_function("verify_installation")

    block_size = 256
    grid_size = int(np.ceil(float(N) / block_size))
    func(a_gpu, b_gpu, c_gpu, np.int32(N),
         block=(block_size, 1, 1), grid=(grid_size, 1))

    # Copy result back to CPU
    cuda.memcpy_dtoh(c, c_gpu)

    # Verify the result
    if np.allclose(c, a + b):
        print("Installation OK")
    else:
        print("Installation FAILED")

check_cuda_devices()
verify_cuda_installation()
