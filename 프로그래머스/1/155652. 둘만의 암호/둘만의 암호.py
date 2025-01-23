def solution(s, skip, index):
    answer = ''
    skip_set = set(skip)  
    for i in range(len(s)):
        current_char = ord(s[i])
        steps = 0
        while steps < index:  
            current_char = (current_char - 97 + 1) % 26 + 97  
            if chr(current_char) not in skip_set:  
                steps += 1
        answer += chr(current_char)
    return answer
