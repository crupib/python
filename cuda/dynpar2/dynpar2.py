import pycuda.driver as cuda
import pycuda.autoinit
from pycuda.compiler import SourceModule
import numpy as np

mod = SourceModule("""
__global__ void parent_kernel() {
    int idx = threadIdx.x + blockIdx.x * blockDim.x;
    printf("Parent kernel execution from thread %d\\n", idx);
}
""")

parent_kernel = mod.get_function("parent_kernel")

def execute_kernel():
    block_size = 10
    grid_size = 1
    parent_kernel(block=(block_size,1,1), grid=(grid_size,1))

def calculate_execution_overhead():
    host_start = cuda.Event()
    host_end = cuda.Event()
    host_start.record()
    execute_kernel()
    host_end.record()
    host_end.synchronize()
    total_time = host_start.time_till(host_end)
    execution_time = 10  # arbitrary, normally you'd get from benchmark
    overhead_time = total_time - execution_time
    xi = overhead_time / execution_time
    print("Execution Overhead xi: ", xi)

def optimize_resource_utilization(resource_allocation):
    utilization = {resource: allocation/100
                   for resource, allocation in resource_allocation.items()}
    utilization_sum = sum(u*w for u,w in
                          zip(utilization.values(), range(1,len(utilization)+1)))
    print("Resource utilization: ", utilization)
    print("Utilization sum: ", utilization_sum)
    return utilization

execute_kernel()
calculate_execution_overhead()
resource_allocation = {'R1':70, 'R2': 50, 'R3':90}
optimize_resource_utilization(resource_allocation)
