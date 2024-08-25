def solution(my_string):
    charset = set()
    answer = []
    for char in my_string:
        if char in charset:
            continue
        
        charset.add(char)
        answer.append(char)
        
    return ''.join(answer)