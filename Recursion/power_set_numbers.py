def power_set(nums: list[int])-> list[list[int]]:
    # we will us recursion and backtracking
    #the idea here is to either take an element or don't take the element
    result = []
    subset = []
    def dfs(i):
        #base case when index goes out of bound
        if i >= len(nums):
            result.append(subset.copy())   #we put a copy of this because all the work is done on the sam esubset array 
            #this creates a deep copy of subset without any reference of the original subset
            return

        #include the element
        subset.append(nums[i])
        dfs(i+1)
        #exlude the element, just remove the one add
        subset.pop()
        dfs(i+1)
    dfs(0)
    return result

if __name__ == '__main__':
    array = list(map(int, input('Enter array in numbers: ').split()))
    ans = power_set(array)
    print(ans)