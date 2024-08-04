def solution(n):
    answer = []
    for i in range(int((n-1)/2)+1):
        answer.append(2*i+1)
    return answer