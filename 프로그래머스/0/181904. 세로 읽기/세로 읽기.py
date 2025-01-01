def solution(my_string, m, c):
    i = c-1
    result =""
    while 1:
        if i<len(my_string):
            result= result+my_string[i]
            i=i+m
        else:
            break
            
            
    return result