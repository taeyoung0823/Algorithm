def sum(list):
    result = 0
    for i in range(len(list)):
        result += list[i]
    return result*result

def mul(list):
    result = 1
    for i in range(len(list)):
        result *= list[i]
    return result

def solution(num_list):
    if sum(num_list)>mul(num_list):
        return 1
    else:
        return 0