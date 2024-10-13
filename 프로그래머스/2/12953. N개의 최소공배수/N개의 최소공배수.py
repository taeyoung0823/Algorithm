def gcd(a, b):
        x=min(a,b)
        y=max(a,b)
        
        if x==0:
            return y
        else:
            return gcd(x,y%x)
        
def lcm(a,b):
    return a*b/gcd(a,b)

def solution(arr):
    result = arr[0]
    for i in range(len(arr)):
        result = lcm(result,arr[i])
        
    return result
        