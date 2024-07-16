def solution(elements):
    answer = 0
    
    s = set()
    
    for i in range(1, len(elements)+1) : # 수열 길이
        for j in range(len(elements)) : # 경우의 수
            if j <= len(elements) - i :
                s.add(sum(elements[j:j+i]))
            else :
                num = i - (len(elements) - j) # 나머지
                s.add(sum(elements[j:]+elements[:num]))
    
    answer = len(s)
    
    return answer