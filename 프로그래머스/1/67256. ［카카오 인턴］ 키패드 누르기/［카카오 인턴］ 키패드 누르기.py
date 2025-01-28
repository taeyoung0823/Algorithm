def cal(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def solution(numbers, hand):
    answer = ''
    result = []
    keypad = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2)
    }
    left_hand = keypad['*']
    right_hand = keypad['#']
    
    for num in numbers:
        if num in [1,4,7]:
            answer += 'L'
            left_hand = keypad[num]
        elif num in [3,6,9]:
            answer += 'R'
            right_hand = keypad[num]
        else:
            target = keypad[num]
            left_dist = cal(left_hand,target)
            right_dist = cal(right_hand,target)
            
            if left_dist < right_dist or (left_dist == right_dist and hand == "left"):
                answer += 'L'
                left_hand = target
            else:
                answer += 'R'
                right_hand = target
                
    return answer