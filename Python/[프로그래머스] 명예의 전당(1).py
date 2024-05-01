def solution(k, score):
    answer = []
    num = []
    for i in range(len(score)) :
        num.append(score[i])
        num.sort(reverse=True)
        if i < k :
            answer.append(num[-1])
        else :
            num = num[:-1]
            answer.append(num[-1])
    return answer