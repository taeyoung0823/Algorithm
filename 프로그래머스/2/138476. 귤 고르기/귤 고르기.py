def solution(k, tangerine):
    answer = 0
    sum_num = 0
    cnt = []
    count = 1
    
    tangerine.sort()
    
    for i in range(1,len(tangerine)):
        if tangerine[i] == tangerine[i-1]:
            count += 1
        else:
            cnt.append(count)
            count = 1
    cnt.append(count)
    
    cnt.sort(reverse=True)
    
    sum_num += cnt[0]
    answer += 1
    for i in range(1,len(cnt)):
        if k > sum_num:
            sum_num += cnt[i]
            answer += 1
        else:
            break
    return answer