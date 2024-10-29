import heapq

def solution(S, K) :
    heap = []
    for i in S :
        heapq.heappush(heap, i)

    answer = 0
    while heap[0] < K :
        if len(heap) == 1 : return -1
    
        heapq.heappush(heap, heapq.heappop(heap) + heapq.heappop(heap) * 2)
        answer += 1
        
    return answer