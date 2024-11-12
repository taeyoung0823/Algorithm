def solution(numbers):
    result = 0
    for i in numbers:
        result += i
    result = result/len(numbers)
    return result