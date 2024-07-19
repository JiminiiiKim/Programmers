# bfs : 숫자 더하거나 뺀 경우를 수평적으로 추가함.

def solution(numbers, target):
    answer = 0
    leaves = [0]
    
    for i in numbers :
        tmp = []
        for parent in leaves :
            tmp.append(parent + i)
            tmp.append(parent - i)
        leaves = tmp
        
    for leaf in leaves :
        if leaf == target :
            answer += 1
            
    return answer