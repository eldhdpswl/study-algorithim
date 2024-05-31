import sys

input = sys.stdin.readline

n, m = map(int, input().split())

A = [[0] * (n+1)]
D = [[0]*(n+1) for _ in range(n+1)]


# 문제에서 좌표를 그대로 대입해서 값을 찾기위해 앞에 배열 안에 0을 넣음
for i in range(n):
    A_row = [0] + [int(x) for x in input().split()]
    # print(A_row)
    A.append(A_row)


for i in range(1, n+1):
    for j in range(1, n+1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]

 
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(result)
