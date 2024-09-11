def jos(n: int,k: int)-> int:
    if n == 1:
        return 0
    else:
        return (jos(n-1, k) + k)%n

if __name__ == '__main__':
    n = int(input('Enter the input n: '))
    k = int(input('Enter k: '))
    print(jos(n,k))
    #if numbering starts from 1 and go to n
    print('If numbering starts fron 1: ',jos(n,k) + 1)