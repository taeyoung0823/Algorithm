def solution(park, routes):
    answer = []
    y = 0
    x = 0
    for i in range(len(park)):        # 초기 위치 설정
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                x = j
                y = i

    for i in range(len(routes)):      # 상하좌우 이동
        direction = routes[i][0]
        distance = int(routes[i][2])
        
        if direction == 'E':
            if x + distance < len(park[0]):  # 범위를 초과하지 않도록 체크
                for j in range(1, distance + 1):  # 이동 경로에 장애물 확인
                    if park[y][x + j] == "X":
                        break
                else:  
                    x += distance
        elif direction == 'W':
            if x - distance >= 0:
                for j in range(1, distance + 1):
                    if park[y][x - j] == "X":
                        break
                else:
                    x -= distance
        elif direction == 'S':
            if y + distance < len(park):
                for j in range(1, distance + 1):
                    if park[y + j][x] == "X":
                        break
                else:
                    y += distance
        else:  # 'N'
            if y - distance >= 0:
                for j in range(1, distance + 1):
                    if park[y - j][x] == "X":
                        break
                else:
                    y -= distance

    answer.append(y)
    answer.append(x)
    return answer
