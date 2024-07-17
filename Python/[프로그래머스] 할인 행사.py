from collections import Counter

def solution(want, number, discount):
    answer = 0
    want_dict = {}
    
    for i in range(len(want)) :
        want_dict[want[i]] = number[i]
    
    for i in range(len(discount)-9) :
        if want_dict == Counter(discount[i:i+10]) :
            answer += 1
    
    return answer