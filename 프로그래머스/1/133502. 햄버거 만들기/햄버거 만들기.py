def solution(ingredient):
    answer = 0
    idx = 0
    while idx < len(ingredient)-3:
        if ingredient[idx:idx+4] == [1,2,3,1]:
            del ingredient[idx:idx+4]
            answer +=1
            if idx < 4:
                idx = 0
            else:
                idx -=3
        else:
            idx+=1    
    return answer
