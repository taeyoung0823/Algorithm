def div(n):
    count = 0
    for i in range(1,n+1):
        if n%i==0:
            count +=1
    return count

def solution(left, right):
    result = 0
    for i in range(left, right + 1):
        if div(i)%2==0:
            result += i
        else:
            result -= i
    return result