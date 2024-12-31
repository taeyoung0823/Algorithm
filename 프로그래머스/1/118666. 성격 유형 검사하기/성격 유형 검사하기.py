def solution(survey, choices):
    result = ""
    scores = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    
    for i in range(len(survey)):
        word = survey[i]
        first = word[0]  
        last = word[1]   
        
        if choices[i] < 4: 
            scores[first] += 4 - choices[i]
        elif choices[i] > 4:  
            scores[last] += choices[i] - 4
            
    if scores['R']<scores['T']:
        result = result+"T"
    else:
        result = result+"R"
        
    if scores['C']<scores['F']:
        result = result+"F"
    else:
        result = result+"C"
    
    if scores['J']<scores['M']:
        result = result+"M"
    else:
        result = result+"J"
    
    if scores['A']<scores['N']:
        result = result+"N"
    else:
        result = result+"A"
    
    return result