def solution(price, money, count):
    result = 0
    i=1
    while i<=count:
        result += i
        i +=1
    answer = price*result-money
    if answer<0:
        return 0
    else:
        return answer