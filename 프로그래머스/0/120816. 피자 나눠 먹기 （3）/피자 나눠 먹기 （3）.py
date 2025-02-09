def solution(slice, n):
    mod = n%slice
    result = n//slice
    if mod != 0:
        return result+1
    else:
        return result