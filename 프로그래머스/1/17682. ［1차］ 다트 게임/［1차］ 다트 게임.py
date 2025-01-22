def solution(dartResult):
    answer = 0
    temp = 0
    old = 0
    oold = 0
    
    for i in range(len(dartResult)):
        if dartResult[i] == 'S':
            temp = temp**1
        elif dartResult[i] == 'D':
            temp = temp**2
        elif dartResult[i] == 'T':
            temp = temp**3
        elif dartResult[i] == '*':
            temp = temp*2
            answer += old
        elif dartResult[i] == '#':
            temp = temp*(-1)
        elif dartResult[i] == '1':
            if dartResult[i+1] == '0':
                if dartResult[i+2] == 'S':
                    answer = answer + temp
                    old = temp
                    temp = 0
                    temp = temp + 10
                elif dartResult[i+2] == 'D':
                    answer = answer + temp
                    old = temp
                    temp = 0
                    temp = temp + 100
                elif dartResult[i+2] == 'T':
                    answer = answer + temp
                    old = temp
                    temp = 0
                    temp = temp + 1000
            else:
                answer = answer + temp
                old = temp
                temp = 0
                temp = temp + 1
        else:
            answer = answer + temp
            old = temp
            temp = 0
            temp = temp + int(dartResult[i])
    if temp !=0 :
        answer += temp
    return answer