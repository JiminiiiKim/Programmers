# [PCCP 기출문제] 1번 / 붕대 감기

def solution(bandage, health, attacks):
    answer = health
    answer -= attacks[0][1]
    
    for i in range(1, len(attacks)) :
        
        # 체력이 0 이하가 되어 죽음.
        if answer <= 0 :
            answer = -1
            return answer
        
        # t : 초당 회복량 적용 횟수, n : 추가 회복량 적용 횟수
        t = attacks[i][0] - attacks[i-1][0] - 1
        n = t // bandage[0]
        if t > 0 :
            answer += (bandage[1] * t)
            answer += (bandage[2] * n)
            # 최대 체력
            if answer > health :
                answer = health
        
        # 피해량 차감
        answer -= attacks[i][1]
        
    return answer