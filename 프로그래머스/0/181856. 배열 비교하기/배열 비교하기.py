def sum(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    return sum

def solution(arr1, arr2):
    if len(arr1)>len(arr2):
        return 1
    elif len(arr1)<len(arr2):
        return -1
    elif len(arr1)==len(arr2):
        if sum(arr1)>sum(arr2):
            return 1
        elif sum(arr1)<sum(arr2):
            return -1
        elif sum(arr1)==sum(arr2):
            return 0