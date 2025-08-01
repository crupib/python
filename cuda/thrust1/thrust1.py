from idlelib.browser import transform_children

import pycuda.autoinit
import pycuda.driver as cuda
import numpy as np
import pycuda.gpuarray as gpuarray
from pycuda.elementwise import ElementwiseKernel

def thrust_like_transform(input_array, scalar,transform_function):
    '''
    Perform a transformation similar to thrust::transform using PyCUDA.
    :param input_array: Input GPU array.
    :param scalar: Scalar multiplier for transformation.
    :param transform_function: Target transformation function in CUDA format.
    :return: Transformed GPU array.
    '''
    transform_kernel = ElementwiseKernel(
        "float *out, float *in, float alpha",
        "out[i] = in[i] + alpha * %s(in[i])" % transform_function,
        "transform_kernel"
    )
    output_array = gpuarray.empty_like(input_array)
    transform_kernel(output_array, input_array, np.float32( scalar))
    return output_array
def thrust_like_reduce(input_array):
    '''
    Perform a reduction transformation equivalent to thrust::reduce to sum array elements.
    :param input_array: Input GPU array.
    :return: Sum of the elements.
    '''
    return gpuarray.sum(input_array).get()
def thrust_like_sort(input_array):
    '''
    Perform a sorting operation similar to thrust::sort using PyCUDA.
    :param input_array: Input array for sorting
    :return: Sorted GPU array.
    '''
    sorted_array = gpuarray.to_gpu(np.sort(input_array.get()))
    return sorted_array

input_size = 1024
host_data = np.random.randn(input_size).astype(np.float32)
device_data = gpuarray.to_gpu(host_data)
transformed_data = thrust_like_transform(device_data, 2.0, "sin")
sum_result = thrust_like_reduce(transformed_data)
sorted_data = thrust_like_sort(transformed_data)
transformed_host_data = transformed_data.get()
sorted_host_data = sorted_data.get()
print("Sum Result:", sum_result)
print("Transformed Data (first 5 elements):", transformed_host_data[:5])
print("Sorted Data (first 5 elements):", sorted_host_data[:5])