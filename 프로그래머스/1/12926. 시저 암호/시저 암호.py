def solution(s, n):
    result = []
    for i in range(len(s)):
        if s[i].isalpha():
            if s[i].islower():
                result.append(chr((ord(s[i])-ord('a')+n)%26+ord('a')))
            elif s[i].isupper():
                result.append(chr((ord(s[i])-ord('A')+n)%26+ord('A')))
        else:
            result.append(s[i])
    return "".join(result)