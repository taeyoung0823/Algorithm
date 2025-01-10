def solution(s):
    diffcount=0
    samecount=1
    totalcount=0
    i=1
    firstindex=0
    while(1):
        if(samecount != diffcount and i==len(s) ):
            totalcount+=1
            
            break
        if(i >= len(s)):
            break
        first=s[firstindex]
        if(first == s[i]):
            samecount+=1
            
        elif(first != s[i]):
            diffcount+=1
            
        if(samecount==diffcount):
            samecount=1
            diffcount=0
            totalcount+=1
            i+=1
            firstindex=i
        i+=1
  
    return totalcount