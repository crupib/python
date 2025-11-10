import os
os.add_dll_directory(r"C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\bin")

import pycuda.driver as cuda
import pycuda.autoinit
import numpy as np
from pycuda.compiler import SourceModule

array_size = 256
host_array = np.random.rand(array_size).astype(np.float32)

d_array = cuda.mem_alloc(host_array.nbytes)
cuda.memcpy_htod(d_array, host_array)

mod = SourceModule("""
extern "C" __global__ void mem_fetch(const float *input, float *output, int n)
{
    int idx = threadIdx.x + blockIdx.x * blockDim.x;
    if (idx < n) {
        output[idx] = input[idx];
    }
}
""")

output = np.zeros_like(host_array)
d_output = cuda.mem_alloc(output.nbytes)

block = (256, 1, 1)
grid = ((array_size + block[0] - 1) // block[0], 1)

func = mod.get_function("mem_fetch")
# pass device pointer to input, device pointer to output
func(d_array, d_output, np.int32(array_size), block=block, grid=grid)

cuda.memcpy_dtoh(output, d_output)

print("equal?", np.allclose(host_array, output))
print("Input Array:\n", host_array)
print("Output Array:\n", output)