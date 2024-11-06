def solution(n):
    result=0
    i=0
    while(n>0):
        result = result + n%10
        n = n//10
    
    return result