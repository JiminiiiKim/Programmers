def solution(s):
    answer = 0
    cre = s[0]
    cnt, cnt2 = 1, 0
    for i in range(1, len(s)-1) :
        if s[i] == cre :
            cnt += 1
        else :
            cnt2 += 1
            if cnt == cnt2 :
                cre = s[i+1]
                cnt, cnt2 = 0, 0
                answer += 1
    answer += 1
        
    return answer