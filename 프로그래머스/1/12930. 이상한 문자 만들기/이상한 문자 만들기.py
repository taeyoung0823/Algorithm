def change(text):
    result = ''
    for i in range(len(text)):
        if i % 2 == 0:
            result += text[i].upper()
        else:
            result += text[i].lower()
    return result

def solution(s):
    answer = ''
    word = ''  

    for char in s:
        if char != ' ':
            word += char 
        else:  
            if word:  
                answer += change(word)
                word = '' 
            answer += char  

    if word:
        answer += change(word)

    return answer
