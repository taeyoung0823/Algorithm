import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    
    while(scoville[0]<K):
        if len(scoville)<2:
            return -1
        else:
            first = heapq.heappop(scoville)
            second = heapq.heappop(scoville)
            
            new = heapq.heappush(scoville, first + 2*second)
            count += 1
    return count