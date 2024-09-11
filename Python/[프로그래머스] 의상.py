def solution(clothes):
    answer = 1
    
    clothes_dict = {}
    for i in clothes :
        if i[1] not in clothes_dict :
            clothes_dict[i[1]] = [i[0]]
        else :
            clothes_dict[i[1]].append(i[0])
    
    
    for i in clothes_dict :
        answer *= (len(clothes_dict[i]) + 1)
    
    return answer-1