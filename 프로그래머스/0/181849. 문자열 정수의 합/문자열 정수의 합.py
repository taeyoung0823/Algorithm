def solution(num_str):
    result = []
    sum = 0
    num = int(num_str)
    while num > 0:
        result.append(num%10)
        num = num//10
    for i in range(len(result)):
        sum += result[i]
    return sum