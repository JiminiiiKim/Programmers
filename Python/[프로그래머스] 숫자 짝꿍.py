def solution(X, Y):
    answer = ''
    x_dict, y_dict = {}, {}
    
    for i in X :
        if i in x_dict :
            x_dict[i] += 1
        else :
            x_dict[i] = 1
    for i in Y :
        if i in y_dict :
            y_dict[i] += 1
        else :
            y_dict[i] = 1
    
    ans = []
    for i in x_dict :
        if i in y_dict :
            min_num = min(x_dict[i], y_dict[i])
            ans += [i] * min_num
            
    if len(ans) == 0 :
        return '-1'
    elif len(ans) == ans.count('0') :
        return '0'
    else :
        ans.sort(reverse=True)
        return "".join(i for i in ans)