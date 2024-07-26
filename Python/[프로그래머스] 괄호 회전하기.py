from collections import deque

def check(temp) :
    str_dict = {'}':'{', ']':'[', ')':'('}
    queue = deque()

    for j in range(len(temp)) :
        if temp[j] in ['[', '(', '{'] :
            queue.append(temp[j])
        else : # 닫는 괄호
            if len(queue) == 0 :
                return 0
            elif str_dict[temp[j]] == queue[-1] :
                queue.pop()
    if len(queue) == 0 : return 1
    else : return 0

def solution(s):
    answer = 0
    
    for i in range(len(s)) :
        temp = s[i:] + s[:i]
        answer += check(temp)

    return answer