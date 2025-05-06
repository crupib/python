import pycuda.driver as cuda
import numpy as np
import pycuda.autoinit
from time import time
size = 1024 * 1024

host_data = np.random.random(size).astype(np.float32)
device_data = cuda.mem_alloc(host_data.nbytes)

def allocate_and_transfer_memory(host_array):
    device_pointer = cuda.mem_alloc(host_array.nbytes)
    cuda.memcpy_htod(device_pointer, host_array)
    return device_pointer

def calculate_bandwidth(num_bytes, transfer_time):
    return num_bytes / (transfer_time * 1e9)

def deallocate_memory(device_pointer):
    device_pointer.free()

def unified_memory_access(array_size):
    managed_array = cuda.pagelocked_zeros(array_size,
            dtype=np.float32, mem_flags=cuda.host_alloc_flags.DEVICEMAP)
    return managed_array

try:
    start_time = time()
    d_ptr = allocate_and_transfer_memory(host_data)
    transfer_time = time() - start_time
    bandwidth = calculate_bandwidth(host_data.nbytes, transfer_time)
    print(f"Effective Bandwidth : {bandwidth:.2f} GB/s")
    unified_array = unified_memory_access(size)
finally:
    deallocate_memory(d_ptr)