from collections import deque

def solution(s):
    q = deque(s[0])
    
    for i in range(1, len(s)) :
        if len(q) == 0 or q[-1] != s[i] :
            q.append(s[i])
        else :
            q.pop()
    
    if len(q) == 0 :
        return 1
    else :
        return 0