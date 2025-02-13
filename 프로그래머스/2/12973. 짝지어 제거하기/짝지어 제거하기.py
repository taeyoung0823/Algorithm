def solution(s):
    s = list(s)  
    j = 0  

    for i in range(len(s)):
        if j > 0 and s[j - 1] == s[i]:  
            j -= 1  
        else:
            s[j] = s[i]  
            j += 1  

    return 1 if j == 0 else 0

