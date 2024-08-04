def solution(my_string):
    L = list(my_string.split())
    x = int(L[0])
    for i in range(1, len(L)-1,2):
        y = int(L[i+1])
        if L[i]=="+": x+=y
        else: x-=y
    return x