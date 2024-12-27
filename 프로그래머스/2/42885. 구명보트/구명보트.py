def solution(people, limit):
    people.sort()
    answer = 0
    
    left = 0
    right = len(people)-1
    while (left != right):
        if left>right:
            break
        else:
            if(people[left]+people[right]<=limit):
                answer += 1
                left += 1
                right -= 1
            else:
                answer+=1
                right -=1
    if left == right:
        answer +=1
    return answer
