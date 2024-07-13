# 최대공약수 구하기
def GCDofnum(a, b) : 
    while b != 0 : 
        a, b = b, a%b 
    return a 
    
def solution(arrayA, arrayB):
    answer = 0
    
    a = arrayA[0]
    for i in range(len(arrayA)) :
        a = GCDofnum(a, arrayA[i])
        
    b = arrayB[0]
    for i in range(len(arrayB)) :
        b = GCDofnum(b, arrayB[i])
    
    for i in range(len(arrayA)) :
        if arrayA[i] % b == 0 :
            b = 0
            break
            
    for i in range(len(arrayB)) :
        if arrayB[i] % a == 0 :
            a = 0
            break
    
    answer = max(a, b)
         
    return answer