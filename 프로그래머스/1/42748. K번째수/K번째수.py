def solution(array, commands):
    sub = []
    result=[]
    for a,b,c in commands:
        sub=array[a-1:b]
        sub.sort()
        result.append(sub[c-1])
    return result