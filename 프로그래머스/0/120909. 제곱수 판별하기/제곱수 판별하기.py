def solution(n):
    answer = 0
    while answer<n:
        for i in range(n):
            if i*i == n:
                return 1
            else:
                answer = i*i
    return 2