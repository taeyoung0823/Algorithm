def num(n):
    for i in range(2,n):
        if n%i==0:
            return 1
    return 0

def solution(n):
    count = 0
    for i in range(0,n+1):
        if num(i)==1:
            count+=1
    return count