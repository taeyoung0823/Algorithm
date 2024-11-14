def solution(n):
    result = 0
    if n%2 == 0:
        for i in range(n+1):
            if i%2==0:
                result += i*i
    else:
        for i in range(n+1):
            if i%2 != 0:
                result += i
                
    return result