def brute_force(start, end):
    freq = [0]*100
    for a,b in zip(start, end):
        for i in range(a, b+1):
            freq[i] += 1
    return freq.index(max(freq))

def efficient(start, end):
    freq = [0] * 101
    for i in range(len(start)):
        freq[start[i]] = 1
        freq[end[i]+1] = -1
    for i in range(len(freq)): #Do a prefix on the frrquency array
        freq[i] = freq[i-1] + freq[i]
    
    return freq.index(max(freq))

print(brute_force([1,2,5,10], [5,8,7,12]))
print(efficient([1,2,5,10], [5,8,7,12]))
