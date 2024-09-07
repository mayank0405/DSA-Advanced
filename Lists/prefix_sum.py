def prefix_sum_brute_force(arr: list[int], s: int, e: int)-> int:
    ans_sum = 0
    while s <= e:
        ans_sum += arr[s]
        s+=1
    return ans_sum

def prefix_sum(arr: list[int], s: int, e: int) -> int:
    pSum = [0]*(len(arr))
    for i in range(len(arr)):
        pSum[i] = pSum[i-1] + arr[i]
    print(pSum)
    if s == 0:
        return pSum[e]
    else:
        return pSum[e] - pSum[s-1]
    
if __name__ == '__main__':
    array = list(map(int, input('Enter the array: ').split()))
    s = int(input('Enter starting point: '))
    e = int(input('Enter ending point: '))
    ans = prefix_sum_brute_force(array, s, e)
    print('Anser through brute force: ', ans)
    ans2 = prefix_sum(array, s, e)
    print('Answer through prefix sum technique: ', ans2)
