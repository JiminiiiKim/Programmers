def solution(s):
    answer = []
    s = s[1:-1].split('{')
    s.sort(key=lambda x : len(x))
    for i in range(1, len(s)) :
        if s[i][-1] == '}' :
            s[i] = list(map(int, s[i][:-1].split(',')))
        else :
            s[i] = list(map(int, s[i][:-2].split(',')))
        for j in s[i] :
            if j not in answer :
                answer.append(j)
    return answer