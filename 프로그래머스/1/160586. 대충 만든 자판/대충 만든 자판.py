def key_idx(alp,keymap):
    min_idx = 1000
    for i in range(len(keymap)):
        for j in range(len(keymap[i])):
            if alp == keymap[i][j]:
                min_idx = min(min_idx,j)
    return min_idx

def solution(keymap, targets):
    answer = []
    for target in targets:
        sum_idx = 0
        for char in target:
            idx = key_idx(char,keymap)
            if idx==1000:
                sum_idx = -1
                break
            sum_idx += idx + 1
        answer.append(sum_idx if sum_idx != -1  else -1)
    return answer