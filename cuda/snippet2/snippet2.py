import pycuda.autoinit
import pycuda.driver as drv
from pycuda.compiler import SourceModule
import numpy as np
import gc  # Garbage collector module
import warnings
warnings.filterwarnings("ignore", category=UserWarning)
# CUDA kernel code
mod = SourceModule("""
__global__ void process_data(float *data, int size) {
    int idx = threadIdx.x + blockIdx.x * blockDim.x;
    if (idx < size) {
        data[idx] = data[idx] * data[idx];
    }
}
""", options=["-arch=sm_75", "--std=c++14", "-w"])  # Adding compilation options


def gpu_square_array(data):
    # Allocate memory on the GPU
    data_gpu = drv.mem_alloc(data.nbytes)

    # Copy data to the GPU
    drv.memcpy_htod(data_gpu, data)

    # Define block and grid sizes
    block_size = 256
    grid_size = (data.size + block_size - 1) // block_size  # Divide by block_size and round up

    # Get the compiled kernel function
    func = mod.get_function("process_data")

    # Launch the kernel
    func(data_gpu, np.int32(data.size), block=(block_size, 1, 1), grid=(grid_size, 1))

    # Allocate memory for output on the host
    data_out = np.empty_like(data)

    # Copy result back to the host
    drv.memcpy_dtoh(data_out, data_gpu)

    # Free the GPU memory
    data_gpu.free()

    return data_out


# Test the function
size = 1000
data = np.random.randn(size).astype(np.float32)
square_array = gpu_square_array(data)

# Print results
print("Original data:", data[:10])
print("Squared data:", square_array[:10])


# Clear CUDA Cache
def clear_cuda_cache():
    global mod
    mod = None  # Delete the SourceModule
    gc.collect()  # Run garbage collection
    drv.Context.synchronize()  # Optional: Synchronize the context


clear_cuda_cache()
