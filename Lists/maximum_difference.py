def maximum_difference_brute_force(l: list[int]) -> int:
    #TC: O(n^2)
    res = l[1] - l[0]
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            diff = l[j] - l[i]
            res = max(res, diff)
    return res

def maximum_difference(l: list[int]) -> int:
    #TC: O(n)
    #find the max and min element and then return difference
    min_element = l[0]
    max_element = l[0]
    for num in l[1:]:
        min_element = min(min_element, num)
        max_element = max(max_element, num)
    return max_element - min_element
if __name__ == '__main__':
    arr = list(map(int, input('Enter array: ').split()))
    print(maximum_difference(arr))