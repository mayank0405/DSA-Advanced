def stringPermutations(str):
    ans = []
    def helper(index):
        if index >= len(str):
            ans.append(''.join(str.copy()))
            return
        for j in range(index, len(str)):
            str[index], str[j] = str[j], str[index]
            helper(index+1)
            str[index], str[j] = str[j], str[index]
    helper(0)
    return ans
        

if __name__ == '__main__':
    string = input('Enter string: ')
    string = list(string)
    ans = stringPermutations(string)
    print(ans)
