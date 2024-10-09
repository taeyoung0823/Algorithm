# 두 배열을 받아서 각 배열에서 숫자를 뽑아서 곱한 값을 더함
# 위 값이 제일 작은 코드를 작성
# 배열 A에서 제일 작은 숫자는 배열 B에서 제일 큰 숫자와 곱해져야함

def solution(A,B):
    A.sort()
    B.sort()
    sum = 0
    for i in range (0,len(A)):
        sum += A[i] * B[len(A)-1-i]
        
    return sum