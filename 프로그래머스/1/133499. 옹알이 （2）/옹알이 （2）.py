def solution(babbling):
    answer = 0
    word = ["aya", "ye", "woo", "ma"]
    
    for i in range(len(babbling)):
        previous_word = ''
        valid = True
        while babbling[i]:
            found = False
            for w in word:
                if babbling[i].startswith(w):  # 현재 단어가 w로 시작하는지 확인
                    if w == previous_word:  # 이전 단어와 동일하면 종료
                        valid = False
                        break
                    previous_word = w
                    babbling[i] = babbling[i][len(w):]  # 단어 제거
                    found = True
                    break
            if not found:  # 일치하는 단어가 없으면 유효하지 않음
                valid = False
                break
        if valid and not babbling[i]:  # 모두 제거되었으면 카운트
            answer += 1
    
    return answer
