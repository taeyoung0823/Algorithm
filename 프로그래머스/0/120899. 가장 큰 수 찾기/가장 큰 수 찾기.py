def solution(array):
    big = 0
    idx = 0
    result = []
    for i in range(len(array)):
        if array[i]>big:
            big = array[i]
            idx = i
    result.append(big)
    result.append(idx)
    return result