def equilibrium_check_brute(arr: list[int]) -> bool:
    for i in range(len(arr)):
        left_sum, right_sum = 0,0
        for j in range(i):
            left_sum += arr[j]
        for k in range(i+1, len(arr)):
            right_sum += arr[k]
        if left_sum == right_sum:
            return True
    return False
def ePoint(arr: list[int])-> bool:
    right_sum = sum(arr)
    left_sum = 0
    for i in range(len(arr)):
        right_sum -= arr[i]
        if right_sum == left_sum:
            return True
        left_sum += arr[i]
    return False
if __name__ == '__main__':
    array = list(map(int, input('Enter array: ').split()))
    ans = equilibrium_check_brute(array)
    print(ans)
    ans2 = ePoint(array)
    print(ans2)