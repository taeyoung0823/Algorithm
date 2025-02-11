def solution(s):
    answer = []
    count = 0
    remove = 0
    
    while s != "1":  
        remove += s.count("0")  
        s = s.replace("0", "")  
        count += 1  
        s = bin(len(s))[2:]
    
    answer.append(count)
    answer.append(remove)
    return answer
