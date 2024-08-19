def least(a, b):
    # 최대공약수
    A, B = a, b
    while b > 0 :
        a, b = b, a % b
    GCD = a 
    # 최소공배수
    return A * B // GCD

def solution(arr) :
    arr.sort()
    temp = arr[0]
    for i in range(0, len(arr)-1) :
        temp = least(temp, arr[i+1])
    return temp