def solution(num_list):
    num_list.sort()
    result = []
    for i in range(5):
        result.append(num_list[i])
    return result