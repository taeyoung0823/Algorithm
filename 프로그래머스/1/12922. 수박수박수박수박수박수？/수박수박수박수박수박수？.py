def solution(n):
    result=[]
    for i in range(1,n+1):
        if i%2 == 0:
            result.append("박")
        else:
            result.append("수")
    return ''.join(result)