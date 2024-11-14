def solution(hp):
    emp = hp//5
    hp = hp - emp*5
    sol = hp//3
    hp = hp - sol*3
    work = hp
    return emp + sol + hp