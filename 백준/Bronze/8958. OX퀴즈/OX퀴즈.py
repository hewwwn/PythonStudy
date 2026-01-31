test=int(input())

for _ in range(test):
    Q=input()
    
    score=0
    conscutive=0
    
    for nx in Q:
        if nx =='O':
            conscutive+=1
            score+=conscutive
        else: 
            conscutive=0
        
    print(score)