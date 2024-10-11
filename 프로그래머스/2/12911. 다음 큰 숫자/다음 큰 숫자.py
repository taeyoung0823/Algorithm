def solution(n):
    i = 0
    k = n
    digit = 0
    count = 0
    
    # 자리수 계산
    while pow(2, i) <= k:
        i += 1
        digit = i
    
    # 1의 개수 계산
    for j in range(digit, 0, -1):
        if k >= pow(2, j-1):
            k = k - pow(2, j-1)
            count += 1
    
    if digit == count:
        return n*2 - int(n/2)
    else:
        c = n
        c0 = c1 = 0
        
        while (c & 1) == 0 and c != 0:
            c0 += 1
            c >>= 1
        
        while (c & 1) == 1:
            c1 += 1
            c >>= 1
        
        
        p = c0 + c1
        n |= (1 << p)  
        n &= ~((1 << p) - 1)  
        n |= (1 << (c1 - 1)) - 1 
        
        return n
