def solution(s):
    answer = []
    
    for i in range(len(s)) :
        # 뒤에서부터 체크
        for j in range(len(answer)-1, -1, -1) :
            if s[i] == s[j] :
                answer.append(i-j)
                break
        if len(answer) != (i+1) :
            answer.append(-1)
            
    return answer