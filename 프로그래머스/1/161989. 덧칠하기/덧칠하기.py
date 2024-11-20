import heapq

def solution(n, m, section):
    heap = []
    for value in section:
        heapq.heappush(heap,value)
    
    count = 0
    while len(heap):
        start = heapq.heappop(heap)
        count += 1

        while heap and heap[0] < start + m:
            heapq.heappop(heap)

    return count