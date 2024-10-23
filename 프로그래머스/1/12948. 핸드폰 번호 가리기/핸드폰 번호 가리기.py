def solution(phone_number):
    k = len(phone_number)-4
    answer = "*" * k + phone_number[-4:]
    return answer