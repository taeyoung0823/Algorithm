def solution(s):
    num = ['zero','one','two','three','four','five','six','seven','eight','nine']
    for i in num:
        if i in s:
            s = s.replace(i, str(num.index(i)))
    return int(s)