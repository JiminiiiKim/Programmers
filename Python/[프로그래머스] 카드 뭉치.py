def check(cards1, cards2, goal) :
    a = []
    idx1, idx2 = 0, 0
    for i in goal :
        if i == cards1[idx1] :
            a.append(i)
            if idx1 < len(cards1)-1 :
                idx1 += 1
        elif i == cards2[idx2] :
            a.append(i)
            if idx2 < len(cards2)-1 :
                idx2 += 1
        else :
            return "No"
    if a == goal :
        return "Yes"
    else : 
        return "No"
    
def solution(cards1, cards2, goal):
    answer = check(cards1, cards2, goal)
    
    return answer