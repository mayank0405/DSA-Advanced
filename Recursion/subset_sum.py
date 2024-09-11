#here we have to tell whther a subset of an array has a sum equal to the given sum of not
def countSubsetSum(arr: list[int], sum, n)->int:
    if n == 0:
        if sum == 0:
            return 1
        else:
            return 0
    return countSubsetSum(arr, sum - arr[n-1], n-1) + countSubsetSum(arr, sum, n - 1)

if __name__ == '__main__':
    array = list(map(int, input('Enter array: ').split()))
    sum = int(input('Enter the sum: '))
    ans = countSubsetSum(array, sum, len(array))
    print(ans)