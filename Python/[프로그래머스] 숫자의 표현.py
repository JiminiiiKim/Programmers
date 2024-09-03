def solution(n):
    answer = 0
    
    for i in range(1, n+1) :
        sum_cont = 0
        for j in range(i, n+1) :
            sum_cont += j
            if sum_cont == n :
                answer += 1
            elif sum_cont > n :
                break
                
    return answer