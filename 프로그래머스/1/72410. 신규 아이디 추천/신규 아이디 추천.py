def solution(new_id):
    answer = ''
    for i in range(len(new_id)):
        if new_id[i].isupper():
            answer += new_id[i].lower()
        elif new_id[i].islower():
            answer += new_id[i]
        elif new_id[i].isdigit():
            answer += new_id[i]
        elif new_id[i] in ['-','_','.']:
            answer += new_id[i]
            
    copy = ''
    for i in range(len(answer)):
        if answer[i] != '.':
            copy += answer[i]
        else:
            if answer [i-1] != '.':
                copy += answer[i]
            else:
                continue
    answer = copy
    
    while 1:
        change = False
        before = len(answer)
        if len(answer) == 0:
            answer += 'a'
            change = True
        elif answer[0] == '.':
            answer = answer[1:]
            change = True
        elif answer [-1] == '.':
            answer = answer[:-1]
            change = True
        
        if len(answer) > 15:
            answer = answer[:15]
            change = True
        elif len(answer) <= 2:
            answer += answer[-1]
            change = True
            
        if change == False and before == len(answer):
            break
        
            
    return answer