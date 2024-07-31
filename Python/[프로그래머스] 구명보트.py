from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    queue = deque(people)
    
    while queue :
        if len(queue) >= 2 :
            if queue[0] + queue[-1] <= limit :
                queue.popleft()
                queue.pop()
                answer += 1
            else : # 무거운 거 제거
                queue.pop()
                answer += 1
        else : # 혼자 남은 거 제거
            queue.pop()
            answer += 1
    
    return answer