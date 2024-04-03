def start_point(row, park) :
    start = [0, 0]

    for i in range(row) :
        if 'S' in park[i] :
            start[0] = i
            start[1] = park[i].index('S')
            return start

def solution(park, routes):
    row = len(park) - 1
    column = len(park[0]) - 1
    start = start_point(row, park)
            
    for r in routes :
        n, m = map(str, r.split())
        m = int(m)
        a = 0
        if (n == 'E') & ((start[1] + m) <= column) :
            for i in range(1, m+1) :
                if park[start[0]][start[1]+i] == 'X' :
                    a = 1
            if a == 0 :
                start[1] += m
        elif (n == 'W') & ((start[1] - m) >= 0) :
            for i in range(1, m+1) :
                if park[start[0]][start[1]-i] == 'X' : 
                    a = 1
            if a == 0 : 
                start[1] -= m
        elif (n == 'S') & ((start[0] + m) <= row) :
            for i in range(1, m+1) :
                if park[start[0]+i][start[1]] == 'X' : 
                    a = 1
            if a == 0 :
                start[0] += m
        elif (n == 'N') & ((start[0] - m) >= 0) :
            for i in range(1, m+1) :
                if park[start[0]-i][start[1]] == 'X' : 
                    a = 1
            if a == 0 :
                start[0] -= m
            
    return start