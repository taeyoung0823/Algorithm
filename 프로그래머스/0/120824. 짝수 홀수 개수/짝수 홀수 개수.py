def solution(num_list):
    odd = 0
    even = 0
    answer = []
    for i in range(len(num_list)):
        if num_list[i]%2==0:
            even +=1
        else:
            odd += 1
    answer.append(even)
    answer.append(odd)
    return answer