def solution(s):
    if len(s) % 2 == 0:
        mid = (len(s)//2)-1
        st = s[mid:mid+2]
        return st
    else:
        mid = len(s)//2
        st = s[mid]
        return st