def solution(n, m, section):
    answer = 0
    cur = section[0]
    
    for i in range(1, len(section)) :
        if (section[i] - cur + 1) > m :
            answer += 1
            cur = section[i]
    answer += 1        
    return answer