def can_place_mat(park, size, start_row, start_col):
    for i in range(start_row, start_row + size):
        for j in range(start_col, start_col + size):
            if park[i][j] != "-1":
                return False
    return True

def solution(mats, park):
    mats.sort(reverse=True)
    rows = len(park)
    cols = len(park[0])

    for mat in mats:
        for i in range(rows - mat + 1):
            for j in range(cols - mat + 1):
                if can_place_mat(park, mat, i, j):
                    return mat
    return -1
