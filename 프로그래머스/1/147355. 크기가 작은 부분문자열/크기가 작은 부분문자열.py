def solution(t, p):
    result = []
    count = 0
    for i in range(0,len(t)-len(p)+1):
        result.append(t[i:i+len(p)])
    number = int(p)
    result = [int(num) for num in result]
    for num in result:
        if number >= num:
            count+=1
    return count