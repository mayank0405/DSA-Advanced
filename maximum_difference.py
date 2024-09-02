def maximum_difference_brute_force(l: list[int]) -> int:
    #TC: O(n^2)
    res = l[1] - l[0]
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            diff = l[j] - l[i]
            res = max(res, diff)
    return res

def maximum_difference_2(l: list[int]) -> int:
    #TC: O(n)
    '''in order to maximise difference, we will need min value so we keep track of min value as well. then we get the 
    difference of min value with each element and then get the max of it. In this way we traverse only once in the array.'''
    res = l[1] - l[0]
    minval = l[0]
    for i in range(1, len(l)):
        res = max(res, l[i]- minval)
        minval = min(minval, l[i])
    return res

if __name__ == '__main__':
    arr = list(map(int, input('Enter array: ').split()))
    print(maximum_difference_brute_force(arr))
    print(maximum_difference_2(arr))