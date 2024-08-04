from collections import deque

def solution(order):
    answer = 0
    wait = []
    cnt = 1
    
    while cnt != len(order) + 1 :
        wait.append(cnt)
        while wait and wait[-1] == order[answer] :
            wait.pop()
            answer += 1
        cnt += 1
    
    return answer