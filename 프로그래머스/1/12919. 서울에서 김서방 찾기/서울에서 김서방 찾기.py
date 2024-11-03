def solution(seoul):
    idx=0
    for i in range(0,len(seoul)):
        if seoul[i] == 'Kim':
            idx = i
    result = "김서방은 "+str(idx)+"에 있다"
    return result