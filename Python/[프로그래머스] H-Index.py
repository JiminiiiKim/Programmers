def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    n = len(citations)
    idx = 0
    
    while idx < n :
        if citations[idx] < (idx+1) :
            return idx 
        idx += 1
        
    return idx