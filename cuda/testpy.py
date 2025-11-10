import os
import ctypes
import numpy as np
import pycuda.driver as cuda
import pycuda.autoinit
from pycuda.compiler import SourceModule

# ===========================
# 1. Set CUDA DLL paths
# ===========================
CUDA_PATH = r"C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v13.0"
os.add_dll_directory(os.path.join(CUDA_PATH, "bin", "x64"))
os.add_dll_directory(os.path.join(CUDA_PATH, "lib", "x64"))

# Optional sanity check
ctypes.WinDLL(os.path.join(CUDA_PATH, "bin", "x64", "cudart64_13.dll"))

# ===========================
# 2. Example kernel
# ===========================
kernel_code = """
__global__ void multiply_by_two(float *data)
{
    int idx = threadIdx.x + blockDim.x * blockIdx.x;
    data[idx] *= 2.0f;
}
"""
mod = SourceModule(kernel_code)
multiply_by_two = mod.get_function("multiply_by_two")

# ===========================
# 3. Host data
# ===========================
N = 16
host_data = np.arange(N, dtype=np.float32)
device_data = cuda.mem_alloc(host_data.nbytes)
cuda.memcpy_htod(device_data, host_data)

# ===========================
# 4. Launch kernel
# ===========================
block_size = 8
grid_size = (N + block_size - 1) // block_size
multiply_by_two(device_data, block=(block_size, 1, 1), grid=(grid_size, 1))

# ===========================
# 5. Retrieve results
# ===========================
result = np.empty_like(host_data)
cuda.memcpy_dtoh(result, device_data)
print("Input : ", host_data)
print("Output: ", result)

# ===========================
# 6. Streams (optional)
# ===========================
stream = cuda.Stream()
cuda.memcpy_htod_async(device_data, host_data, stream)
multiply_by_two(device_data, block=(block_size, 1, 1), grid=(grid_size, 1), stream=stream)
cuda.memcpy_dtoh_async(result, device_data, stream)
stream.synchronize()
print("Output with stream: ", result)
