def prime(num):
    for i in range(2,num):
        if num%i==0:
            return 1
    return 2

def solution(nums):
    answer = 0
    count = 0
    for i in range(0,len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):
                answer = nums[i]+nums[j]+nums[k]
                
                if prime(answer)==2:
                    count +=1
    return count