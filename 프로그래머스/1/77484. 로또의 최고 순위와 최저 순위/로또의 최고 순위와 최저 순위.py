# 로또 최고 함수
# 배열 두개 입력 받아서, 정렬 후 같은 숫자의 개수를 리턴
def lotto_good(str1,str2):
    str1.sort()
    str2.sort()
    count = 0
    for i in range(len(str1)):
        if str1[i] in str2:
            count +=1
    for i in range(len(str1)):
        if str1[i]==0:
            count+=1
    return count

# 로또 최악 함수
# 배열 두개 입력 받아서, 정렬 후 같은 숫자의 개수를 리턴
def lotto_bad(str1,str2):
    str1.sort()
    str2.sort()
    count = 0
    for i in range(len(str1)):
        if str1[i] in str2:
            count +=1
    return count

# 랭크 함수
# 일치하는 숫자 입력 받아서 등수 리턴
def rank(n):
    if n==6:
        return 1
    elif n==5:
        return 2
    elif n==4:
        return 3
    elif n==3:
        return 4
    elif n==2:
        return 5
    else:
        return 6

def solution(lottos, win_nums):
    result = []
    num1 = lotto_good(lottos, win_nums)
    num2 = lotto_bad(lottos, win_nums)
    result.append(rank(num1))
    result.append(rank(num2))
    return result