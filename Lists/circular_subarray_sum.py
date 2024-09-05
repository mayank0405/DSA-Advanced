def maxSum_kadane(arr: list[int]) -> int:
    maxSum = arr[0]
    currSum = arr[0]
    for i in range(1, len(arr)):
        currSum = max(currSum + arr[i], arr[i])
        maxSum = max(currSum, maxSum)
    return maxSum

def minSum_kadane(arr: list[int]) -> int:
    minSum = arr[0]
    currSum = arr[0]
    for i in range(1, len(arr)):
        currSum = min(currSum + arr[i], arr[i])
        minSum = min(currSum, minSum)
    return minSum

def maxSubarraySumCircular(nums: list[int]) -> int:
    maximum_subarray_sum = maxSum_kadane(nums)
    if maximum_subarray_sum < 0:
        return maximum_subarray_sum
    total_array_sum = sum(nums)
    minimum_subarray_sum = minSum_kadane(nums)
    circular_sum = total_array_sum - minimum_subarray_sum
    return max(maximum_subarray_sum, circular_sum)

if __name__ == '__main__':
    arr = list(map(int, input('Enter array: ').split()))
    ans = maxSubarraySumCircular(arr)
    print(ans)

    
               
