def solution(food):
    result = []
    for i in range(1,len(food)):
        num = food[i]//2
        for j in range(0,num):
            result.append(i)
    left = result
    right = sorted(result, reverse=True)
     
    answer = left + [0] + right
    return ''.join(map(str, answer))