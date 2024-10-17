def solution(numbers):
    sum = 0
    for i in numbers:
        sum += i
        
    result = 45 - sum
    return result