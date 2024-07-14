N, M = map(int, input().split())
B =[0]*(N+1)

for _ in range(M):
    i, j, k = map(int, input().split())
    for n in range(i, j+1):
        B[n] = k
        
for i in range(1, N+1):
    print(B[i], end=" ")