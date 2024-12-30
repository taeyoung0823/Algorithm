def binary(n, length):
    return bin(n)[2:].zfill(length)

def solution(n, arr1, arr2):
    result = []
    for i in range(len(arr1)):
        change = (arr1[i] | arr2[i])
        result.append(binary(change, n).replace('1', '#').replace('0', ' '))
    return result
