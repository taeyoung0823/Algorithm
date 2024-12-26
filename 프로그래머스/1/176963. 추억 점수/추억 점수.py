def solution(name, yearning, photo):
    answer = []
    for i in range(len(photo)):
        total_score = 0
        for person in photo[i]:
            if person in name:
                total_score += yearning[name.index(person)]
        answer.append(total_score)
    return answer
