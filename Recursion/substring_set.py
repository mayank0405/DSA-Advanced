#This is similar to the power set
def substring(str: str)-> list[str]:
    result = []
    def dfs(index, curr):
        if index >= len(str):
            result.append(curr)
            return
        dfs(index+1, curr+ str[index])
        dfs(index+1, curr)
    dfs(0, '')
    return result


if __name__ == '__main__':
    string = input('Enter the string: ')
    ans = substring(string)
    print(ans)