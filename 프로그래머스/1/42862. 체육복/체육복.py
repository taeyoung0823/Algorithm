def solution(n, lost, reserve):
    answer = n
    copy = lost[:]
    for item in copy:
        if item in reserve:
            reserve.remove(item)
            lost.remove(item)
            
    lost.sort()
    reserve.sort()
    
    for i in range(len(lost)):
        if lost[i]-1 in reserve:
            reserve.remove(lost[i]-1)
            continue
        elif lost[i]+1 in reserve:
            reserve.remove(lost[i]+1)
            continue
        else:
            answer -= 1
    return answer