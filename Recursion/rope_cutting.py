def maxPieces(n: int, a: int, b: int, c: int)-> int:
    if n < 0:
        return -1
    if n == 0:
        return 0
    res  = max(maxPieces(n-a, a,b,c), maxPieces(n-b,a,b,c), maxPieces(n-c,a,b,c))
    if res == -1: #this handles the case where a,b,c are equal. If none of the options work (res == -1), return -1
        return -1
    return res + 1

if __name__ == '__main__':
    n,a,b,c = list(map(int, input('Enter in the following order: n a b c: ').split()))
    ans = maxPieces(n,a,b,c)
    print(ans)
