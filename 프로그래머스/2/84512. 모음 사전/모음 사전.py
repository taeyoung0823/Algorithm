def solution(word):
    answer = 0
    lst=['A','E','I','O','U']
    for i in range(len(word)):
        for j in range(len(lst)):
            if word[i] == lst[j]:
                if i==0:
                    answer += 781*j + 1
                elif i==1:
                    answer += 156*j + 1
                elif i==2:
                    answer += 31*j + 1
                elif i==3:
                    answer += 6*j + 1
                elif i==4:
                    answer += j + 1
    return answer