# 가장 많이 받은 선물
def solution(friends, gifts):
    answer = 0
    # 선물 주고 받은 내역이 담긴 배열
    arr = [[0 for j in range(len(friends))] for i in range(len(friends))]
    for i in gifts :
        give, receive = i.split(' ')
        arr[friends.index(give)][friends.index(receive)] += 1
   
   # 선물 지수 계산
    arr2 = [0] * len(friends)
    for i in range(len(friends)) :
        row_sum, col_sum = 0, 0
        for j in range(len(friends)) :
            row_sum += arr[i][j]
            col_sum += arr[j][i]
        arr2[i] = row_sum - col_sum
    
    final = [0] * len(friends)
    for i in range(len(friends)) :
        for j in range(i+1, len(friends)) :
            if arr[i][j] > arr[j][i] : # A가 더 많이 선물을 줌.
                final[i] += 1
            elif arr[i][j] == arr[j][i] : # A, B가 선물 준 횟수가 같음.
                if arr2[i] > arr2[j] : # A가 더 선물 지수가 높음.
                    final[i] += 1
                elif arr2[i] < arr2[j] : # B가 더 선물 지수가 높음.
                    final[j] += 1
            else : # B가 더 많이 줌.
                final[j] += 1
   
    answer = max(final)
                
    return answer