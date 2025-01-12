def solution(X, Y):
    count_y = [0] * 10
    for char in Y:
        count_y[int(char)] += 1

    result = []
    for char in X:
        digit = int(char)
        if count_y[digit] > 0:  
            result.append(char)
            count_y[digit] -= 1 

    result.sort(reverse=True)

    if not result:
        return '-1'
    if result[0] == '0':
        return '0'
    
    return ''.join(result)
