L =[]
for i in range(10):
    x = int(input())
    L.append(x%42)
L = set(L)
print(len(L))