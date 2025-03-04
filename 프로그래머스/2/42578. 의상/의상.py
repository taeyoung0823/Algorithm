def solution(clothes):
    answer = 1
    clothes_dict = {}
    
    for item, category in clothes:
        if category not in clothes_dict:
            clothes_dict[category] = []
        
        clothes_dict[category].append(item)
    
    for category in clothes_dict:
        answer *= (len(clothes_dict[category]) + 1)  
    
    return answer - 1