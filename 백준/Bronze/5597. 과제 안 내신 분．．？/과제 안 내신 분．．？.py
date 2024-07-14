S =[]
for i in range(31):
    S.append(i)
S.remove(0)

for i in range(28):
    n = int(input())
    S.remove(n)
    
print(min(S))
print(max(S))