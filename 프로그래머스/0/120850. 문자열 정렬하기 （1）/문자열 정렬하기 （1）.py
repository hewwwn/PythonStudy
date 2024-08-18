def solution(my_string):
    return list(sorted(int(x) for x in my_string if x.isdigit()))