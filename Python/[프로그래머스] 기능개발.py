from collections import deque

def solution(progresses, speeds):
    answer = []
        
    pro = deque(progresses)
    speed = deque(speeds)
    
    while pro :
        num = 0
        
        for i in range(len(pro)) :
            pro[i] += speed[i]
            
        while pro and pro[0] >= 100 :
                pro.popleft()
                speed.popleft()
                num += 1
                
        if num != 0 :
            answer.append(num)
    
    return answer