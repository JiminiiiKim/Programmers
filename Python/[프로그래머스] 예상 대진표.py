def solution(n,a,b):
    answer = 1

    while n != 2 :
        if a % 2 == 0 : # 짝수
            if b == a-1 :
                return answer
        else : # 홀수
            if b == a+1 :
                return answer
        a, b = (a + 1) // 2, (b + 1) // 2
        answer += 1

    return answer