def solution(a, b):
    answer = 0
    i=0
    while 1:
        if b < 10**i:
            first = a*10**i + b
            break
        else:
            i+=1
    i=0
    while 1:
        if a < 10**i:
            second = b*10**i + a
            break
        else:
            i+=1
    print(first)
    print(second)
    return max(first,second)