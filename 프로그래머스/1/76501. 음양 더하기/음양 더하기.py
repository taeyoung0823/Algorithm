def solution(absolutes, signs):
    sum=0
    for i in range(0,len(absolutes)):
        if signs[i] == True:
            sum += absolutes[i]
        else:
            sum -= absolutes[i]
        i += 1
    return sum