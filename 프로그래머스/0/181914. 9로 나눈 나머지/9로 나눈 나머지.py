def solution(number):
    result = 0
    answer = int(number)
    while answer>0:
        result += answer % 10
        answer = answer // 10
    result = result % 9
    return result