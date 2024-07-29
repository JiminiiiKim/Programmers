def solution(s):
    answer = []
    
    cnt = s.count('0')
    num = len(s) - cnt
    rnd = 1
    
    while num != 1 :
        bin_num = str(format(num, 'b'))
        num_0 = bin_num.count('0')
        cnt += num_0
        num = len(bin_num) - num_0
        rnd += 1
    
    answer = [rnd, cnt]
                
    return answer