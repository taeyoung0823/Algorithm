def solution(wallpaper):
    answer = []
    min_x = len(wallpaper)
    max_x = 0           
    min_y = len(wallpaper[0])
    max_y = 0   

    for i in range(len(wallpaper)):  
        for j in range(len(wallpaper[0])):  
            if wallpaper[i][j] == '#':
                min_x = min(min_x, i)
                max_x = max(max_x, i)
                min_y = min(min_y, j)
                max_y = max(max_y, j)

    answer = [min_x, min_y, max_x + 1, max_y + 1] 
    return answer
