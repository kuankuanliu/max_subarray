import sys
import time

# Usage when run from the command line: python max_subarray_homework1.py <filename>.
# Example usage:                        python max_subarray_homework1.py num_array_500.txt

file_name = sys.argv[1]

f = open(file_name, "r")
A = [int(num) for num in f.readline().strip().split(" ")]
f.close()

def max_subarray_enumeration(A):
    """
    Computes the value of a maximum subarray of the input array by "enumeration."
    
    Parameters:
        A: A list (array) of n >= 1 integers.
    
    Returns:
        The sum of the elements in a maximum subarray of A.
    """

    # TODO: Implement this function!
    max_sum_e = float("-inf")
    for i in range(len(A)):
        for j in range(i, len(A)):
            cur_sum = 0
            for k in range(i, j + 1):
                cur_sum +=A[k]
                max_sum_e = max(max_sum_e, cur_sum)
                if max_sum_e == cur_sum:
                    start, end = i, j + 1
    return A[start: end], max_sum_e
    
def max_subarray_iteration(A):
    """
    Computes the value of a maximum subarray of the input array by "iteration."
    
    Parameters:
        A: A list (array) of n >= 1 integers.
    
    Returns:
        The sum of the elements in a maximum subarray of A.
    """

    # TODO: Implement this function!
    max_sum_i = float("-inf")
    for i in range(len(A)):
        cur_sum = 0
        for j in range(i, len(A)):
            cur_sum += A[j]
            max_sum_i = max(max_sum_i, cur_sum)
            if max_sum_i == cur_sum:
                start, end = i, j + 1
    return A[start: end],max_sum_i


def time_alg(alg, A):
    """
    Runs an algorithm for the maximum subarray problem on a test array and times how long it takes.
    
    Parameters:
        alg: An algorithm for the maximum subarray problem.
        A: A list (array) of n >= 1 integers.
    
    Returns:
        A pair consisting of the value of alg(A) and the time needed to execute alg(A) in milliseconds.
    """

    start_time = time.monotonic_ns() // (10 ** 6) # The start time in milliseconds.
    max_subarray_val = alg(A)
    end_time   = time.monotonic_ns() // (10 ** 6) # The end time in milliseconds.
    return max_subarray_val, end_time - start_time

for alg in [max_subarray_enumeration, max_subarray_iteration]:
    print(file_name, time_alg(alg, A))

