def day(num):
    a = num%7
    return a

def solution(a, b):
    result = 0
    while a!=1:
        if a==2:
            a -= 1
            b += 31
        elif a==3:
            a -= 1
            b += 29
        elif a==4:
            a -= 1
            b += 31
        elif a==5:
            a -= 1
            b += 30
        elif a==6:
            a -= 1
            b += 31
        elif a==7:
            a -= 1
            b += 30
        elif a==8:
            a -= 1
            b += 31
        elif a==9:
            a -= 1
            b += 31
        elif a==10:
            a -= 1
            b += 30
        elif a==11:
            a -= 1
            b += 31
        elif a==12:
            a -= 1
            b += 30
            
    result += b
    
    if day(result)==0:
        return "THU"
    elif day(result)==1:
        return "FRI"
    elif day(result)==2:
        return "SAT"
    elif day(result)==3:
        return "SUN"
    elif day(result)==4:
        return "MON"
    elif day(result)==5:
        return "TUE"
    elif day(result)==6:
        return "WED"
    