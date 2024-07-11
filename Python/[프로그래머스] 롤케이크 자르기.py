# set 함수 : 시간 초과
# dp 2개 : 메모리 초과

from collections import Counter
 
def solution(topping):
    answer = 0
    set1 = Counter(topping) 
    set2 = set()
    
    for i in topping :
        set1[i] -= 1
        set2.add(i)
        
        if set1[i] == 0:
            set1.pop(i)
            
        if len(set1) == len(set2):
            answer += 1
            
    return answer