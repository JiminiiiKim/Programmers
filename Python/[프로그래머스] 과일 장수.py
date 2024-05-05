def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    for i in range(0, len(score), m) :
        if i+m <= len(score) :
            num = min(score[i:i+m])
            answer += num * m
    return answer