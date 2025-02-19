def win(n):
    if n%2==0:
        return n/2
    else:
        return (n+1)/2

def solution(n,a,b):
    answer = 1
    min_num = min(a,b)
    max_num = max(a,b)
    while min_num+1 != max_num:
        a = win(a)
        b = win(b)
        min_num = min(a,b)
        max_num = max(a,b)
        answer +=1
    
    while 1:
        if max_num%2!=0:
            max_num=win(max_num)
            answer+=1
        else:
            break

    return answer