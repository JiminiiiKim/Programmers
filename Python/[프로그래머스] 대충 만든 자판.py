def solution(keymap, targets):
    answer = [0] * len(targets)
    
    for idx in range(len(targets)) :
        for word in targets[idx] :
            cnt = 0
            # 모든 keymap에서 각 단어 확인
            for key in keymap :
                if word in key :
                    if cnt != 0 :
                        if cnt >= key.index(word) + 1 :
                            cnt = key.index(word) + 1
                    else :
                        cnt = key.index(word) + 1  
                # 없으면 계속
                else :
                    continue
            # 없으면 -1
            if cnt == 0 :
                answer[idx] = -1
            else :
                if answer[idx] != -1 :
                    answer[idx] += cnt
    

    return answer