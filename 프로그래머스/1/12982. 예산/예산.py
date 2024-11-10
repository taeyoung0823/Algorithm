def solution(d, budget):
    d.sort()
    result = 0
    sum = 0
    for k in range(0,len(d)):
        sum += d[k]
    
    if sum == budget or sum < budget:
        return len(d)
    else:
        for i in range(0,len(d)):
            if budget-d[i] >= 0:
                budget = budget - d[i]
                result += 1
            else:
                return result