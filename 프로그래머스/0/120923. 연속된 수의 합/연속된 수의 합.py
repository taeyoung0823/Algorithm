def sum_num(n):
    result = 0
    for i in range(n):
        result += i
    return result

def solution(num, total):
    answer = []
    numb = 0
    for i in range(-100,100):
        if (num*i)+sum_num(num) == total:
            numb = i
            break
    
    for i in range(num):
        answer.append(numb)
        numb += 1
    
    
    return answer
    