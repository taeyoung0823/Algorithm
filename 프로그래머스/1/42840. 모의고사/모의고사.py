def comp_A(answers):
    A = [1,2,3,4,5]
    result = 0
    for i in range(len(answers)):
        if answers[i] == A[i%5]:
            result +=1
    return result

def comp_B(answers):
    B = [2,1,2,3,2,4,2,5]
    result = 0
    for i in range(len(answers)):
        if answers[i] == B[i%8]:
            result +=1
    return result

def comp_C(answers):
    C = [3,3,1,1,2,2,4,4,5,5]
    result = 0
    for i in range(len(answers)):
        if answers[i] == C[i%10]:
            result +=1
    return result


def solution(answers):
    answer = []
    great = max(comp_A(answers),comp_B(answers),comp_C(answers))
    if great == comp_A(answers):
        answer.append(1)
    if great == comp_B(answers):
        answer.append(2)
    if great == comp_C(answers):
        answer.append(3)
    
    return answer