import pycuda.autoinit
import pycuda.driver as cuda
import numpy as np
from pycuda.compiler import SourceModule
mod  = SourceModule("""  __global__ void calculate_eta(int *warp_results, float *eta) {
    int idx = threadIdx.x;
    __shared__ int results[32];
    results[idx] = warp_results[idx];
    __syncthreads();
    int active_count = 0;
    for (int i = 0; i < 32; i++) {
      active_count += results[i];
    }
    if (idx == 0) {
      eta[0] = active_count/32.0;
    }
  }
  __global__ void calculate_execution_efficiency(int total_instructions, int divergent_branches, float *efficiency) {
    efficiency[0] = (total_instructions - divergent_branches) / (float)total_instructions; 
  }
  __global__ void manage_latency(float load, float overhead, float eta, float *latency) {
    latency[0] = (load + overhead)/eta;
 }
 __global__ void optimize_tasks(int *task_arr, int n) {
   int idx = threadIdx.x + blockIdx.x * blockDim.x;
   if (idx < n) {
      task_arr[idx] = task_arr[idx] * 2;
   }
 }
 __global__ void enforce_warp_sync(int *data) {
   int idx = threadIdx.x;
   __syncwarp();
   data[idx] += 1;
 }
 """)

task_arr = np.array([1,2,3,4,5,6,7,8], dtype=np.int32)
task_arr_gpu = cuda.mem_alloc(task_arr.nbytes)
cuda.memcpy_htod(task_arr_gpu, task_arr)
optimize_tasks = mod.get_function("optimize_tasks")
optimize_tasks(task_arr_gpu, np.int32(len(task_arr)), block=(8,1,1), grid=(1,1))
optimize_tasks_arr = np.empty_like(task_arr)
cuda.memcpy_dtoh(optimize_tasks_arr, task_arr_gpu)
print("Optimized Tasks:",optimize_tasks_arr)

warp_results = np.random.randint(0,2,size=32).astype(np.int32)
eta = np.zeros(1).astype(np.float32)
warp_results_gpu = cuda.mem_alloc(warp_results.nbytes)
eta_gpu = cuda.mem_alloc(eta.nbytes)
cuda.memcpy_htod(warp_results_gpu, warp_results)
calculate_eta = mod.get_function("calculate_eta")
calculate_eta(warp_results_gpu, eta_gpu, block=(32,1,1))
cuda.memcpy_dtoh(eta,eta_gpu)
print("Warp Efficiency:",eta[0])

execution_efficiency = np.zeros(1).astype(np.float32)
calulate_execution_efficiency = mod.get_function("calculate_execution_efficiency")
calulate_execution_efficiency(np.int32(100), np.int32(10),cuda.Out(execution_efficiency),block=(1,1,1))
print("Execution Efficiency ():",execution_efficiency[0])
latency = np.zeros(1).astype(np.float32)
manage_latency = mod.get_function("manage_latency")
manage_latency(np.float32(500), np.int32(10), eta, cuda.Out(latency),block=(1,1,1))
print("Latency ():",latency[0])

data = np.arange(32).astype(np.int32)
data_gpu = cuda.mem_alloc(data.nbytes)
cuda.memcpy_htod(data_gpu, data)
enforce_warp_sync = mod.get_function("enforce_warp_sync")
enforce_warp_sync(data_gpu, block=(32,1,1))
cuda.memcpy_dtoh(data, data_gpu)
print("Data after sync:",data)
