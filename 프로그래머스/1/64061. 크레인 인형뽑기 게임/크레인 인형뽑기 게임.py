def solution(board, moves):
    answer = 0
    result = []

    for i in range(len(moves)):
        for j in range(len(board)):
            if board[j][moves[i]-1] != 0:
                result.append(board[j][moves[i]-1])
                board[j][moves[i]-1] = 0
                break

    while True:
        new_lst = []
        skip = False
        for i in range(len(result) - 1):
            if skip:
                skip = False
                continue
            if result[i] == result[i + 1]:
                answer += 2
                skip = True
            else:
                new_lst.append(result[i])
        if not skip and result:
            new_lst.append(result[-1])

        if len(new_lst) == len(result):
            break
        result = new_lst

    return answer
