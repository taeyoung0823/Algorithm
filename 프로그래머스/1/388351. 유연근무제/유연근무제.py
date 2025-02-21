def solution(schedules, timelogs, startday):
    deadline = []
    result = 0
    diff = startday-1
    
    for i in range(len(schedules)):
        schedules[i] = schedules[i]+10
        if schedules[i]%100 >= 60:
            schedules[i] += 40
        deadline.append(schedules[i])
    
    for i in range(len(timelogs)):
        count = 0
        for j in range(len(timelogs[0])):
            if timelogs[i][j]>deadline[i]:
                if (j+diff)%7==0 or (j+diff)%7 == 1 or (j+diff)%7 == 2 or (j+diff)%7 == 3 or (j+diff)%7 == 4:
                    count +=1
        if count == 0:
            result += 1
    return result