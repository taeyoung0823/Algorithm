import math

def solution(n, m):
    result = []
    gcd = math.gcd(n,m)
    lcm = n * m / gcd
    result.append(gcd)
    result.append(lcm)
    return result