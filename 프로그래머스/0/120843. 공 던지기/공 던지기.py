def solution(numbers, k):
    answer = 0
    i=0
    a=0
    while a!=k-1:
        i = i+2
        i = i%len(numbers)
        a = a+1
    i = i+1
    return i