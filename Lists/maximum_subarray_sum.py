from math import inf
def maxSum(nums: list[int], n: int) -> int:
    sum = 0
    maxi = nums[0]
    for i in range(n):
        sum = sum + arr[i] #Step -1
        maxi = max(maxi, sum) #Step -2
        if sum < 0: #Step -3 if the sum is -ve then forget it. if we add it to sum it will only decrease the max_sum
            sum = 0
    return maxi

if __name__ == '__main__':
    arr = list(map(int, input('Enter array: ').split()))
    array_length = len(arr)
    ans = maxSum(arr, array_length)
    print(ans)