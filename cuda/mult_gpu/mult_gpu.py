# Multiple GPUS
import pycuda.driver as cuda
import numpy as np
from pycuda.compiler import SourceModule
cuda.init()
num_gpus = cuda.Device.count()
if num_gpus < 2:
    raise RuntimeError("Not enough GPUs available")
contexts = [cuda.Device(i).make_context() for i in range(num_gpus)]
kernel_code = """
__global__ void gpu_task(float *data, int n) {
    int idx = threadIdx.x + blockIdx.x * blockDim.x;
    if (idx < n) {
        data[idx] = data[idx] * 2.0;
    }
}
"""
mod = SourceModule(kernel_code)
gpu_task = mod.get_function("gpu_test")


def allocate_and_upload(data):
    gpu_data = cuda.mem_alloc(data.nbytes)
    cuda.memcpy.htod(gpu_data, data)
    return gpu_data


task_size = 1024
tasks = [np.random.rand(task_size).astype(np.float32) for i in range(num_gpus)]
gpu_data = [allocate_and_upload(task) for task in tasks]
for i in range(num_gpus):
    contexts[i].push()
    gpu_task(gpu_data[i], np.int32(task_size), block=(256, 1, 1), grid=(4, 1))
    contexts[i].pop()
results = []
for i in range(num_gpus):
    results = np.empty_like(tasks[i])
    contexts[i].push()
    results.append(results)
for context in contexts:
    context.pop()
for i, result in enumerate(results):
    print(f"Result from GPU {i}:")
    print(result[:10])
