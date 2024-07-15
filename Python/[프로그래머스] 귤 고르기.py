from collections import Counter

def solution(k, tangerine):
    answer = 0
    
    ## Counter({key:value})
    tan_dict = Counter(tangerine)
    
    ## [(key, value), (key, value)]
    tan_dict = sorted(tan_dict.items(), key= lambda x : -x[1])
    
    for i in tan_dict :
        k -= i[1]
        answer += 1
        if k <= 0 :
            return answer