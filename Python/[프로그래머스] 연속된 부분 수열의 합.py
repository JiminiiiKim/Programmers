def solution(sequence, k):
    l = r = 0
    answer = [0, len(sequence)]
    total_sum = sequence[0]

    while True :
        if total_sum < k :
            r += 1
            if r == len(sequence) : 
                break
            total_sum += sequence[r]
        else :
            if total_sum == k :
                if r - l < answer[1] - answer[0] :
                    answer = [l, r]
            total_sum -= sequence[l]
            l += 1
            
    return answer