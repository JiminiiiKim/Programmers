def solution(record):
    answer = []
    user_dict = {}
    
    for i in record :
        state = i.split(" ")
        if state[0] == 'Enter' :
            user_dict[state[1]] = state[2]
            answer.append(state[1] + ' e')
        elif state[0] == 'Leave' :
            answer.append(state[1] + ' l')
        elif state[0] == 'Change' :
            user_dict[state[1]] = state[2]
            
    for i in range(len(answer)) :
        state = answer[i].split(" ")
        if state[1] == 'e' :
            answer[i] = user_dict[state[0]] +'님이 들어왔습니다.'
        elif state[1] == 'l' :
            answer[i] = user_dict[state[0]] + '님이 나갔습니다.'
    
    return answer