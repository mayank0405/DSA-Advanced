def subset_sum(arr: list[int], target: int) -> int:
    n = len(arr)
    power_set = []
    subset = []
    
    # Depth First Search to generate all subsets
    def dfs(i):
        if i >= n:
            power_set.append(subset.copy())
            return
        # Include the element
        subset.append(arr[i])
        dfs(i + 1)
        # Exclude the element
        subset.pop()
        dfs(i + 1)

    dfs(0)
    
    # Print all subsets
    print("Generated Power Set: ", power_set)
    
    count = 0
    # Count how many subsets sum up to the target
    for sub in power_set:
        if sum(sub) == target:
            count += 1

    return count

if __name__ == '__main__':
    nums = list(map(int, input('Enter array: ').split()))
    sum = int(input('Enter sum: '))
    ans = subset_sum(nums, sum)
    print(ans)

