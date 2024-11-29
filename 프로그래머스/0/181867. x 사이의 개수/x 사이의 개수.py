def solution(myString):
    answer = []
    count = 0
    for i in range(len(myString)):
        if myString[i] == 'x' :
            if i == len(myString)-1:
                answer.append(count)
                answer.append(0)
            else:
                answer.append(count)
                count = 0
        else:
            if i == len(myString)-1:
                count+=1
                answer.append(count)
            else:
                count +=1
    
    return answer