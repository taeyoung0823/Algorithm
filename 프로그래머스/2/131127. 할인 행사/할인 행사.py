def solution(want, number, discount):
    count = 0
    want_dict = {want[i]: number[i] for i in range(len(want))}
    
    for i in range(len(discount)-9):
        disc_item = discount[i:i+10]
        disc_list = {}
        
        for item in disc_item:
            if item in disc_list:
                disc_list[item] += 1
            else:
                disc_list[item] = 1 
    
        if all(disc_list.get(item, 0) >= want_dict[item] for item in want_dict):
            count +=1
            
    return count