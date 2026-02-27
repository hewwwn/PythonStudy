import sys
input=sys.stdin.readline

N=input().strip()
cnt=[0]*10

for i in N:
    pn=int(i)
    cnt[pn]+=1
    
    
six_nine = cnt[6] + cnt[9]
cnt[6]= (six_nine+1)//2
cnt[9]= 0

print(max(cnt))

