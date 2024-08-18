def solution(array):
    return max(array), max(range(len(array)), key=lambda i: array[i])