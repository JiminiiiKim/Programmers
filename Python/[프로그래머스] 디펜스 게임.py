from heapq import heappush, heappop

def solution(n, k, enemy):
    answer, sum_enemy = 0, 0
    heap = []
    for i in enemy :
        heappush(heap, -i)
        sum_enemy += i
        if sum_enemy > n :
            if k == 0 : break
            sum_enemy += heappop(heap)
            k -= 1
        answer += 1
            
    return answer