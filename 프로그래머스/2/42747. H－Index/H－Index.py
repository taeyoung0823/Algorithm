def solution(citations):
    max = 0
    citations.sort()
    
    
    if len(citations)<citations[0]:
        return len(citations)
    
    for i in range(len(citations)):
        cnt = 0
        for j in range(len(citations)):
            if citations[j]>=i:
                cnt +=1
        if i <= cnt:
            if max < i:
                max = i
    return max