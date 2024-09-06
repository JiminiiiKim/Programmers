from collections import deque

def solution(priorities, location):
    answer = 0
    q, prior = deque([i for i in range(len(priorities))]), deque(priorities)
    a = False
    
    while a == False :
        cur, cur_prior = q.popleft(), prior.popleft()
        if q and cur_prior < max(prior) :
            prior.append(cur_prior)
            q.append(cur)
        else : # 우선순위 가장 높음.
            if cur == location :
                answer += 1
                a = True
            else :
                answer += 1
                
    return answer