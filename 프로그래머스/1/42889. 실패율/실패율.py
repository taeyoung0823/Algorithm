def solution(N, stages):
    n_stage = {}
    challenger = len(stages)
    
    for i in range(1, N + 1):
        if challenger != 0:
            fail_num = stages.count(i)
            n_stage[i] = fail_num / challenger
            challenger -= fail_num
        else:
            n_stage[i] = 0
    
    result = sorted(n_stage.keys(), key=lambda x: n_stage[x], reverse=True)
    
    return result
