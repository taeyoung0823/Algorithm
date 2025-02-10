def solution(s):
    s.lower()
    answer = ''
    if s[0].isalpha():
        answer += s[0].upper()
    else:
        answer += s[0]
    for i in range(1,len(s)):
        if s[i].isalpha() and s[i-1] == ' ':
            answer += s[i].upper()     
        else:
            answer += s[i].lower()
                
    return answer