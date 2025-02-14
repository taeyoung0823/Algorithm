def solution(brown, yellow):
    result = []
    answer = []
    width = []
    sum = brown + yellow
    min_difference = float('inf')  # 초기 최소 차이를 무한대로 설정
    
    
    # 가능한 약수를 찾기
    for i in range(2, sum // 2 + 1):
        if sum % i == 0:
            result.append(i)
    
    # 조건을 만족하면서 차이가 최소인 경우만 선택
    for i in range(len(result)):
        for j in range(i, len(result)):
            if result[i] * result[j] == sum and (result[i]-2)*(result[j]-2)== yellow:
                difference = abs(result[i] - result[j])
                if difference < min_difference:
                    min_difference = difference
                    answer = [max(result[i], result[j]), min(result[i], result[j])]
    

    return answer
