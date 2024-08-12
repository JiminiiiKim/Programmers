def solution(s):
    answer = True
    stack = []
    
    for i in s :
        if i == '(' :
            stack.append(i)
        else :
            if stack : stack.pop()
            else : return False
        
    if len(stack) != 0 : 
        return False
    return True