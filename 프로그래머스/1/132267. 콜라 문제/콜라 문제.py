
def solution(a, b, n):
    result=0
    while n>=a:
        result += b*(n//a)
        n = n%a + b*(n//a)
    return result