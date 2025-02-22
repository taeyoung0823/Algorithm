def solution(my_string):
    answer = ''
    vowel = ['a','e','i','o','u']
    for i in range(len(my_string)):
        if my_string[i] in vowel:
            continue
        else:
            answer += my_string[i]
    return answer