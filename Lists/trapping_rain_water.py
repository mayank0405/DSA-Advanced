def trapping_rain_water(arr: list[int], n: int) -> int:
    if n == 0:
        return 0
    
    res = 0
    left = [0] * n
    right = [0] * n

    left[0] = arr[0]
    for i in range(1, n):
        left[i] = max(left[i-1], arr[i])

    right[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        right[i] = max(right[i+1], arr[i])

    for i in range(1, n-1):
        res += min(left[i], right[i]) - arr[i]

    return res

if __name__ == '__main__':
    a = list(map(int, input('Enter the list: ').split()))
    ans = trapping_rain_water(a, len(a))
    print(ans)
