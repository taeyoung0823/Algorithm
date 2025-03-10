def solution(t, p):
    result = []
    count = 0
    for i in range(0,len(t)-len(p)+1):
        if int(p) >= int(t[i:i+len(p)]):
            count+=1
    return count