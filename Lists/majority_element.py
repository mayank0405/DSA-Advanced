def majority_element(v: list[int]) -> int:
        count = 0
        ele = -1
        for i in range(len(v)):
            if count == 0:
                ele = v[i]
                count = 1
            if ele == v[i]:
                count += 1
            else:
                count -= 1
        
        #checking the candidate
        x = 0
        for i in range(len(v)):
            if v[i] == ele:
                count += 1
        if count > len(v)//2:
            return ele
        return -1

if __name__ == '__main__':
    arr = list(map(int, input('Enter array: ').split()))
    ans = majority_element(arr)
    print(ans)
