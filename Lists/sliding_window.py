import math

def sliding_window_brute_force(nums: list[int], n: int, k: int) -> int:
    maxTotal = -math.inf
    for i in range(n-k+1):
        total = sum(nums[i: i+k])
        maxTotal = max(maxTotal, total)
    return maxTotal

def sliding_window(nums: list[int], n: int, k: int) -> int:
    maxSum = -math.inf
    curr_sum = 0
    for i in range(k):
        curr_sum += nums[i]
    maxSum = max(maxSum, curr_sum)
    for j in range(k, n):
        curr_sum = curr_sum + arr[j] - arr[j-k]
        maxSum = max(maxSum, curr_sum)
    return maxSum

if __name__ == '__main__':
    arr = list(map(int, input('Enter the array: ').split()))
    k = int(input('Enter k: '))
    arr_len = len(arr)
    ans = sliding_window_brute_force(arr, arr_len, k)
    print(ans)
    ans2 = sliding_window(arr, arr_len, k)
    print(ans2)
