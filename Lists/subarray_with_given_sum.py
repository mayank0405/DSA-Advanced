def brute_force(arr: list[int], sum: int)-> bool:
    for i in range(len(arr)):
        curr_sum = 0
        for j in range(i, len(arr)):
            curr_sum += arr[j]
            if curr_sum == sum:
                return True
    return False

def optimal(arr: list[int], sum: int)-> bool:
    curr_sum = 0
    s,e = 0,0
    while curr_sum < sum:
        curr_sum += arr[e]
        e+=1
    while curr_sum > sum:
        curr_sum = curr_sum - arr[s]
        s = s + 1
    if curr_sum == sum:
        return True
    else:
        return False


if __name__ == '__main__':
    arr = list(map(int, input('Enter the array: ').split()))
    check_sum = int(input('Enter the check sum: '))
    print(brute_force(arr, check_sum))
    print(optimal(arr, check_sum))