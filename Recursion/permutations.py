def permutations(nums: list[int])->list[list[int]]:
    permutations = []
    def func(index):
        if index >= len(nums):
            permutations.append(nums.copy())
            return
        for j in range(index, len(nums)):
            nums[index], nums[j] = nums[j], nums[index]
            func(index + 1)
            nums[index], nums[j] = nums[j], nums[index]
    func(0)
    return permutations

if __name__ == '__main__':
    array = list(map(int, input('Enter array: ').split()))
    ans = permutations(array)
    print(ans)