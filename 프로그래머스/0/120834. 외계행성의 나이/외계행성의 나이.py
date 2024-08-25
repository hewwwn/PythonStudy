def solution(age):
    n2char = {str(i):char for i, char in enumerate('abcdefghij')}
    print(n2char)
    return ''.join(n2char[n] for n in str(age))