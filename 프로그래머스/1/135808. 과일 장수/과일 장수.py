def solution(k, m, score):
    score.sort()
    result = 0
    n=len(score)
    start = 0
    end = n
    
    while end-start>=m:
            result += score[end-m]*m
            end -= m
            
    return result