import sys
input = sys.stdin.readline

N=int(input())
card_n=list(map(int,input().split()))
M=int(input())
card_m=list(map(int,input().split()))

card_dict = {}

for i in card_n:
    if i in card_dict:
        card_dict[i]+=1
    else:
        card_dict[i]=1
        
        
result = []
for i in card_m:
    if i in card_dict:
        result.append(str(card_dict[i]))
    else:
        result.append("0")
print(" ".join(result))