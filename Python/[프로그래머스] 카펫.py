def solution(brown, yellow):
    answer = []
    a, b = 0, 0
    cnt = 1
    while a * b != (brown + yellow) and cnt <= yellow :
        if yellow % cnt == 0 :
            yellow_a, yellow_b = yellow // cnt, cnt
            a, b = (yellow_a + 2), (yellow_b + 2)
        cnt += 1
    answer = [a, b]
    return answer