def solution(n):
    answer = ''
    num = ['1', '2', '4']
    
    while n != 0 :
        n -= 1
        n, r = n // 3, n % 3
        answer = num[r] + answer
        
    return answer