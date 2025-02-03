def solution(bandage, health, attacks):
    answer = 0 # 최종 체력
    hp = health # 현재 체력
    count = 0 # 연속 체력 화복 
    limit = attacks[-1][0] # 몬스터의 마지막 공격 시간 (초)
    attacks_second = []
    attacks_power = []
    j = 0
    
    for i in range(len(attacks)):
        attacks_second.append(attacks[i][0])
        attacks_power.append(attacks[i][1])
    
    for i in range(0,limit+1):
        if i in attacks_second:
                hp -= attacks[j][1]
                j += 1
                count = 0
        else:
            if hp + bandage[1] < health:
                hp += bandage[1]
                count += 1
            else:
                hp = health
                count += 1
                
        if count == bandage[0]:
            hp += bandage[2]
            count = 0
        if hp > health:
            hp = health
        if hp<=0:
            return -1
        print(hp)
        
                
    
    return hp