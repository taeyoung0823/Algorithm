def solution(s):
    arr = list(map(int, s.split(' ')))
    arr.sort()
    a=arr[0]
    b=arr[-1]
    c=str(a)+" "+str(b)
    
    return c