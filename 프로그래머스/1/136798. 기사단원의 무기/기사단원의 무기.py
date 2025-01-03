def div(n):
    count = 0
    for div in range(1, int(n**0.5) + 1):
        if n % div == 0:
            count += 2 if div != n // div else 1  

    return count

def solution(number, limit, power):
    result = 0
    for i in range(1,number+1):
        if div(i)>limit:
            result+=power
        else:
            result += div(i)
    return result