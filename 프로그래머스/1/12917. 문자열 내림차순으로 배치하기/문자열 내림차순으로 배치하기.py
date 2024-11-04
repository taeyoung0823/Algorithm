def solution(s):
    result = []
    for i in range(0,len(s)):
        result.append(s[i])
        i += 1
    result.sort(reverse=True)
    return ''.join(result)