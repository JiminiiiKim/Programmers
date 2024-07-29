def solution(A, B):
    answer = 0
    temp = B
    
    for i in range(1, len(B)+1) :
        if temp == A :
            return answer
        temp = B[i:] + B[:i]
        answer += 1
    answer = -1
    return answer