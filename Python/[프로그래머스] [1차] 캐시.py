from collections import deque
def solution(cacheSize, cities):
    answer = 0
    
    cities = [i.lower() for i in cities]
    q = deque(cities[:cacheSize])
    uni = len(set(q))
    answer += (uni * 5 + (cacheSize-uni))
        
    for i in range(cacheSize, len(cities)) :
        if cities[i] in q :
            q.remove(cities[i])
            q.append(cities[i])
            answer += 1
        else :
            answer += 5
            if cacheSize != 0 :
                q.popleft()
                q.append(cities[i])
        
    return answer