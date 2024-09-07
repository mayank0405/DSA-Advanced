def prefix_sum(arr: list[int])-> list[int]:
    pSum = [0]*len(arr)
    pSum[0] = arr[0]
    for i in range(1, len(arr)):
        pSum[i] = pSum[i-1] + arr[i]
    return pSum

def weighted_sum(arr: list[int], s: int, e: int) -> int:
    prefix_sum_array = prefix_sum(arr)
    get_sum = 0
    for i in range(e):
        get_sum += (i - s + 1)*prefix_sum_array[i]
    return get_sum


if __name__ == '__main__':
    array = list(map(int, input('Enter the array: ').split()))
    start = int(input('Enter starting index: '))
    end = int(input('Enter ending index: '))
    ans = weighted_sum(array, start, end)
    print(f'Weighted sum is: {ans}')