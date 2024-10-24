def solution(n):
    k=[]
    result=0
    while (n>0):
        a = n%10
        n = n//10
        k.append(a)
        
    k.sort()
    k.reverse()
    for i in range(0,len(k)):
        result = result + k[i]
        if i != len(k)-1:
            result = result*10

    return result