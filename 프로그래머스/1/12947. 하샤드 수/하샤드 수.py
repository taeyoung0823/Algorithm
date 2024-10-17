def solution(x):
    num = x
    sum = 0
    while(x!=0):
        if 0<x<10:
            sum = sum + x
            x = 0
        else:
            sum = sum + x%10
            x = (x-x%10)/10
    
    if num%sum == 0:
        return True
    else :
        return False
        