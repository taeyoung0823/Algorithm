def solution(angle):
    if angle>180:
        angle -= 180
    elif 0<angle and angle<90:
        return 1
    elif angle == 90:
        return 2
    elif 90<angle and angle<180:
        return 3
    else:
        return 4
    return answer