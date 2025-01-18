def solution(n):
    answer = 0
    lst = []
    while(n>0):
        lst.append(n%3)
        n = n//3
    
    for i in range(len(lst)):
        answer += lst[i] * (3 ** (len(lst)-i-1))
        
    return answer