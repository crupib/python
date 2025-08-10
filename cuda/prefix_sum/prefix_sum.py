import os
os.add_dll_directory(r"C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\bin")

import numpy as np
import pycuda.driver as cuda
import pycuda.autoinit
from pycuda.compiler import SourceModule

kern_src = r"""
extern "C" {

__global__ void upsweep(float* data, int n, int step) {
    int gap = step << 1;
    int k   = blockIdx.x * blockDim.x + threadIdx.x;
    int idx = k * gap + (gap - 1);
    if (idx < n) {
        data[idx] += data[idx - step];
    }
}

__global__ void downsweep(float* data, int n, int step) {
    int gap = step << 1;
    int k   = blockIdx.x * blockDim.x + threadIdx.x;
    int idx = k * gap + (gap - 1);
    if (idx < n) {
        float t            = data[idx - step];
        data[idx - step]   = data[idx];
        data[idx]         += t;
    }
}

} // extern "C"
"""

def gpu_prefix_sum(arr):
    # NOTE: requires n to be a power of two
    h = np.asarray(arr, dtype=np.float32)
    n = h.size
    assert (n & (n - 1)) == 0, "Blelloch kernel below assumes power-of-two length"

    d = cuda.mem_alloc(h.nbytes)
    cuda.memcpy_htod(d, h)

    mod = SourceModule(kern_src)
    upsweep   = mod.get_function("upsweep")
    downsweep = mod.get_function("downsweep")

    block = 256

    # --- Upsweep (reduce) ---
    step = 1
    while step < n:
        gap = step << 1
        # number of active idx = n / gap (ceil not needed; n, gap are powers of two)
        active = n // gap
        grid = (active + block - 1) // block
        if active > 0:
            upsweep(d, np.int32(n), np.int32(step), block=(block,1,1), grid=(grid,1))
        step <<= 1

    # set last element to 0 (exclusive scan)
    cuda.memset_d32(int(d) + (n - 1) * h.itemsize, 0, 1)

    # --- Downsweep ---
    step >>= 1
    while step > 0:
        gap = step << 1
        active = n // gap
        grid = (active + block - 1) // block
        if active > 0:
            downsweep(d, np.int32(n), np.int32(step), block=(block,1,1), grid=(grid,1))
        step >>= 1

    out = np.empty_like(h)
    cuda.memcpy_dtoh(out, d)
    return out

if __name__ == "__main__":
    input_array = np.array([1,2,3,4,5,6,7,8], dtype=np.float32)
    output_array = gpu_prefix_sum(input_array)
    print("Input:", input_array.tolist())
    print("Exclusive prefix sum:", output_array.tolist())
