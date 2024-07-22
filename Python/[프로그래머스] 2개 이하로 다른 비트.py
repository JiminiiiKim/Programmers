# 시간 초과 : 81.8점
"""def solution(numbers):
    answer = []
    for i in numbers :
        a = True
        x = i
        
        while a :
            x += 1
            num = i^x # XOR 연산자
            cnt = 0
            # 이진수에서 1의 개수 구하기
            while num > 0 : 
                if num % 2 == 1 :
                    cnt += 1
                num //= 2
            if cnt <= 2 :
                answer.append(x)
                a = False
                
    return answer"""

def solution(numbers):
    answer = []

    for i in numbers :
        if i % 2 == 0 : # 짝수
            answer.append(i + 1)
        else : # 홀수
            num_bin = '0' + bin(i)[2:]
            # 처음으로 '01'이 나온 지점을 '10'으로 바꿈.
            num_bin = num_bin[:num_bin.rindex('0')] + '10' + num_bin[num_bin.rindex('0')+2:]
            answer.append(int(num_bin, 2))

    return answer