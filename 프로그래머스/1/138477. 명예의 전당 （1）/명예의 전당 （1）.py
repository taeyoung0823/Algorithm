def solution(k, score):
    rank = []
    result = []
    
    for i in range(len(score)):
        if len(rank) < k:
            rank.append(score[i])
        else:
            if score[i] > min(rank):
                rank.remove(min(rank))
                rank.append(score[i])
        
        rank.sort()
        result.append(min(rank))
    
    return result
