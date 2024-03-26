# 단순히 list.index()는 시간 초과
# 딕셔너리로 바꿔서 생각하기

def solution(players, callings):
    answer = {player : i for i, player in enumerate(players)}
    
    for calling in callings : 
        idx = answer[calling]
        answer[calling] -= 1
        answer[players[idx-1]] += 1
        players[idx-1], players[idx] = players[idx], players[idx-1]
    
    return players