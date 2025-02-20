def solution(elements):
    answer = set()
    len_ele = len(elements)
    
    for i in range(len_ele-2):
        elements.append(elements[i])
    
    for i in range(1,len_ele+1):
        for j in range(len_ele):
            sum_num = sum(elements[j:j+i])
            answer.add(sum_num)
            
    
    return len(answer)