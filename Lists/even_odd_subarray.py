def even_odd(arr: list[int], n: int)-> int:
    count, s_count = 1,1
    for i in range(1, n):
        if (arr[i-1] & 1 == 0 and arr[i] & 1 != 0) or (arr[i-1] & 1 != 0 and arr[i] & 1 == 0):
            s_count += 1
            count = max(s_count, count)
        else:
            s_count = 1
    return count

if __name__ == '__main__':
    arr = list(map(int, input('Enter array: ').split()))
    array_length = len(arr)
    ans = even_odd(arr, array_length)
    print(ans)

    