def solution(num_list):
    answer = 0
    even = 0
    odd = 0
    for i in range(len(num_list)):
        if num_list[i]%2==0:
            even *= 10
            even += num_list[i]
        else:
            odd *= 10
            odd += num_list[i]
    return even+odd