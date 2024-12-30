import math

def gcd(a, b):
    return math.gcd(a, b)

def lcm(a, b):
    return a * b // gcd(a, b)

def solution(numer1, denom1, numer2, denom2):
    result = []
    num = lcm(denom1, denom2)
    first = numer1 * (num // denom1)
    second = numer2 * (num // denom2)
    numerator_sum = first + second
    greatest_common_divisor = gcd(numerator_sum, num)
    result.append(numerator_sum // greatest_common_divisor)
    result.append(num // greatest_common_divisor)
    
    return result