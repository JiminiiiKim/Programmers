def rotate(num) :
    return (num - 96) % 26 + 97

def solution(s, skip, index):
    answer = ''

    for i in s:        
        num = ord(i)
        # 한 칸씩 이동하며 확인
        for j in range(index) :
            num = rotate(num)
            while chr(num) in skip:
                num = rotate(num)
        answer += chr(num)

    return answer