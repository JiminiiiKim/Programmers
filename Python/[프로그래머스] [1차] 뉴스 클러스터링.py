def convert_list(s) : 
    s_list = []
    s = s.lower()

    for i in range(len(s)-1) :
        if s[i] >= 'a' and s[i] <= 'z' :
            if s[i+1] >= 'a' and s[i+1] <= 'z' :
                s_list.append(s[i]+s[i+1])
    return s_list
    
def solution(str1, str2):
    answer = 0
    str1_list, str2_list = convert_list(str1), convert_list(str2)
    
    if len(str1_list) == 0 and len(str2_list) == 0 :
        return 65536
    
    inter_set = set(str1_list) & set(str2_list)
    
    inter = 0
    for i in inter_set :
        inter += min(str1_list.count(i), str2_list.count(i))
    
    answer = int(inter / (len(str1_list) + len(str2_list) - inter) * 65536)
    
    return answer