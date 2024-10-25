from collections import deque

def solution (numbers, target):
    queue = deque([(0,0)])
    ways_to_target = 0
    
    while queue:
        current_sum, idx = queue.popleft()
        
        if idx == len(numbers):
            if current_sum == target:
                ways_to_target += 1
                
        else:
            queue.append((current_sum + numbers[idx], idx + 1))
            queue.append((current_sum - numbers[idx], idx + 1))
                
    
    return ways_to_target