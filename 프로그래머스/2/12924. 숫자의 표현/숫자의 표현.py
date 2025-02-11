def solution(n):
    answer = 1
    for i in range(1,n//2+2):
        total = 0
        for j in range(i,n+1):
            if total<n:
                total += j
            elif total==n:
                answer+=1
                break
            else:
                break
            
    return answer