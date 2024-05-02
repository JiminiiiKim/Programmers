def solution(number, limit, power):
    answer = 0
    num = []
    
    for i in range(1, number+1) :
        cnt = 0
        for j in range(1, i//2+1) :
            if i % j == 0 :
                cnt += 1
                if j**2 != i :
                    cnt += 1
                if cnt > limit :
                    num.append(power)
                    break
        num.append(cnt)
          
    answer = sum(num)
    
    return answer