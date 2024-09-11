def tower_of_hanoi(n: int, A,B,C)-> None:
    if n == 1:
        print('Move 1 from A to C')

    else:
        #now we will move top n-1 discs from A to B using C
        tower_of_hanoi(n-1, A, C, B)
        # Now move the nth disc from A to C
        print(f'Move {n} from A to C')
        #Move the rest of discs from B to C using A
        tower_of_hanoi(n-1, B, A, C)

if __name__ == '__main__':
    n = int(input('Enter number of dics: '))
    tower_of_hanoi(n, 'A', 'B', 'C')