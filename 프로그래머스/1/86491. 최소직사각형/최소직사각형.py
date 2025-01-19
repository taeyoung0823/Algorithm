def solution(sizes):
    answer = 0 # 최종 결과 값 담을 변수
    width = 0 # 가로 값
    height = 0 # 세로 값
    
    for i in range(len(sizes)):
        if sizes[i][1]>sizes[i][0]: #뒤에 숫자가 더 클 경우 
            sizes[i][0],sizes[i][1] = sizes[i][1],sizes[i][0] #앞 뒤 자리 바꾸기
        if sizes[i][0]>width: # for문 돌면서 큰 값으로 바꿔주기
            width = sizes[i][0]
        if sizes[i][1]>height:
            height = sizes[i][1]
        else:
            continue
            
    answer = width * height # 가로 * 세로
        
    return answer