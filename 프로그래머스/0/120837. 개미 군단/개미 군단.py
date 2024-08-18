def solution(hp):
    ant = 0
    
    ant += hp//5
    hp = hp % 5
    
    ant += hp//3
    hp = hp % 3
    
    ant += hp//1
    return ant