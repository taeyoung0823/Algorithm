#7           7
#3 8         10 15
#8 1 0       18 16 15
#2 7 4 4     20 25 20 19
#4 5 2 6 5   24 30 27 26 24

def solution(triangle):
    answer = triangle
    for i in range(0,len(triangle)):
        for j in range(0,i+1):
            if i==j:
                if i>=1:
                    answer[i][j] = answer[i-1][j-1]+triangle[i][j]
            elif j==0:
                answer[i][j] = answer[i-1][j]+triangle[i][j]
            else:
                answer[i][j] = max(answer[i-1][j-1]+triangle[i][j],answer[i-1][j]+triangle[i][j])
    result = max(answer[len(triangle)-1])
    return result