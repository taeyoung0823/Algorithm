def solution(nums):
    unique_nums = list(set(nums))
    a = len(unique_nums)
    b = len(nums)//2
    return min(a,b)