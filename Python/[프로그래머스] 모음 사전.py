def solution(word):
    answer = 0
    dic = {'A':0, 'E':1, 'I':2, 'O':3, 'U':4}
    li = [5**i for i in range(len(dic))]
    
    for i in range(len(word)-1, -1, -1) :
        idx = dic[word[i]]
        
        for j in range(5-i) :
            answer += li[j] * idx
        
        answer += 1
        
    return answer