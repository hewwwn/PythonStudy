def solution(my_string):
    my_string = sorted(x.lower() for x in my_string)
    return ''.join(my_string)