import math

def solution(fees, records):
    answer = []
    user_dict = {}
    
    for i in records : # 기록 dict 생성
        temp = i.split(' ')
        time = list(map(int, temp[0].split(':')))
        time = time[0] * 60 + time[1]
        if temp[1] not in user_dict :
            user_dict[temp[1]] = [time]
        else :
            user_dict[temp[1]].append(time)
            
    user_dict = dict(sorted(user_dict.items()))
    
    for i in user_dict :
        time = 0
        if len(user_dict[i]) % 2 == 1 : # 출차 기록 없음.
            user_dict[i].append(23*60+59)
        for j in range(0, len(user_dict[i]), 2) : # 누적 주차 시간 계산
            time += (user_dict[i][j+1] - user_dict[i][j])
        if time > fees[0] : # 기본 시간 이상
            answer.append(fees[1] + math.ceil((time - fees[0])/fees[2]) * fees[3])
        else :
            answer.append(fees[1])
        
    return answer