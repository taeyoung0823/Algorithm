def solution(start_num, end_num):
    answer = []
    now=start_num
    while now != end_num-1:
        answer.append(now)
        now -=1
    return answer