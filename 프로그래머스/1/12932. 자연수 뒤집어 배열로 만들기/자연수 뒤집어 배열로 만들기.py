def solution(n):
    answer = []
    while(n>0):
        k=0
        k=n%10
        n = n//10
        answer.append(k)
    return answer