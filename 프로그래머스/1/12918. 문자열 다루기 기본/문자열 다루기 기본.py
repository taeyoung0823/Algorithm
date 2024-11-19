def solution(s):
    try:
        int(s)
    except ValueError:
        return False
    else:
        if len(s) == 4 or len(s) == 6:
            return True
        else:
            return False