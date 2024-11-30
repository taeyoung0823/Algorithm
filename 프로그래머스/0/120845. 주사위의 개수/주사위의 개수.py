def solution(box, n):
    a = box[0]//n
    b = box[1]//n
    c = box[2]//n
    box = a*b*c
    return box