def left_rotate_1(l: list[int], d: int) -> list[int]:
    #using slicing
    d = d%len(l)
    return l[d:] + l[:d]

def left_rotate_2(l: list[int], d: int) -> list[int]:
    #reversing concept
    #we can also reverse from 0 to d. then d to n-1. then reverse the whole list
    if d == 0:
        return l
    d = d%len(l)
    reverse(l, 0, len(l)-1)
    reverse(l, 0, d)
    reverse(l, d+1, len(l)-1)
    return l

def reverse(a, s, e):
    while s <= e:
        a[s], a[e] = a[e], a[s]
        s+=1
        e-=1

if __name__ == '__main__':
    arr = list(map(int, input('Enter array: ').split()))
    d = int(input('Enter d: '))
    print(left_rotate_1(arr, d))
    print(left_rotate_2(arr, d))
               
    
