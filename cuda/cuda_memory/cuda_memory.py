import numpy as np
import pycuda.driver as cuda
import pycuda.autoinit
from pycuda.compiler import SourceModule
import warnings
warnings.filterwarnings("ignore", category=UserWarning)
# CUDA Kernel Code
mod = SourceModule("""
__global__ void simple_kernel(float *a, float *b, float *c, int N) {
    int idx = blockIdx.x * blockDim.x + threadIdx.x;
    if (idx < N) {
        c[idx] = a[idx] + b[idx];
    }
}
""", options=["-arch=sm_75", "--std=c++14", "-w"])

# Input data
N = 1024
a_host = np.random.randn(N).astype(np.float32)
b_host = np.random.randn(N).astype(np.float32)

# Allocate pinned memory
a_pinned = cuda.pagelocked_empty_like(a_host)
b_pinned = cuda.pagelocked_empty_like(b_host)
np.copyto(a_pinned, a_host)
np.copyto(b_pinned, b_host)

# Allocate memory on the device
a_device = cuda.mem_alloc(a_host.nbytes)
b_device = cuda.mem_alloc(b_host.nbytes)
c_device = cuda.mem_alloc(a_host.nbytes)

# Copy data to device
stream = cuda.Stream()
cuda.memcpy_htod_async(a_device, a_pinned, stream)
cuda.memcpy_htod_async(b_device, b_pinned, stream)

# Launch kernel
function = mod.get_function("simple_kernel")
block_size = 256
grid_size = (N + block_size - 1) // block_size
function(a_device, b_device, c_device, np.int32(N), block=(block_size, 1, 1), grid=(grid_size, 1), stream=stream)

# Copy result back to host
c_host = np.empty_like(a_host)
cuda.memcpy_dtoh_async(c_host, c_device, stream)
stream.synchronize()

# Cleanup
a_device.free()
b_device.free()
c_device.free()

# Verify result
print("Computation complete. Results:", c_host[:10])
