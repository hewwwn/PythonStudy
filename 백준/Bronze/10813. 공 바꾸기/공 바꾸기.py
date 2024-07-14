N, M = map(int, input().split())
B = [i for i in range(1, N+1)]

for i in range(M):
    i, j = map(int, input().split())
    B[i - 1], B[j - 1] = B[j - 1], B[i - 1]

for i in range(N):
    print(B[i], end=" ")