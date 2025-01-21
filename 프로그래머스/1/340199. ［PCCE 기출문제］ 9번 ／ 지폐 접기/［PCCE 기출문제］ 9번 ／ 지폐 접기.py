def solution(wallet, bill):
    answer = 0
    if wallet[0]<wallet[1]:
        wallet[0],wallet[1] = wallet[1],wallet[0]
    while(1):
        if bill[0]<bill[1]:
            bill[0],bill[1] = bill[1],bill[0]
        
        if bill[0]>wallet[0]:
            bill[0] = bill[0]//2
            answer += 1
        elif bill[1]>wallet[1]:
            bill[0] = bill[0]//2
            answer += 1
        else:
            break
    return answer