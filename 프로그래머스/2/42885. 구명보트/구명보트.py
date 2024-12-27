from collections import deque

def solution(people, limit):
    people = deque(sorted(people))  # deque로 변환 후 정렬
    answer = 0

    while people:
        if len(people) == 1:  # 남은 사람이 한 명일 경우
            people.pop()
            answer += 1
        elif people[0] + people[-1] <= limit:  # 가장 가벼운 사람 + 가장 무거운 사람
            people.popleft()  # 가장 가벼운 사람 제거
            people.pop()  # 가장 무거운 사람 제거
            answer += 1
        else:  # 가장 무거운 사람만 태울 경우
            people.pop()
            answer += 1

    return answer
