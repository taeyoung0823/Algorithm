def solution(money):
    answer = []
    ice = money//5500
    ex = money%5500
    answer.append(ice)
    answer.append(ex)
    return answer