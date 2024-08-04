def solution(array):
    answer = 0
    arr = []
    count = {}
    for i in array:
        if i not in count : 
            count[i] = 1
        else :
            count[i] += 1
    count = sorted(count.items(), key = lambda x : x[1], reverse = True)
    print(count)
    if len(count) > 1 and count[0][1] == count[1][1] :
        return -1
    else :
        return count[0][0]
        