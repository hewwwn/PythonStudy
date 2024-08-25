def solution(num, k):
    ans = -1
    for i, c in enumerate(str(num), 1):
        if int(c) == k:
            ans = i
            break
            
    return ans