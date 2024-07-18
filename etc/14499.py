import sys
input = sys.stdin.readline

N, M, x, y, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
lst = list(map(int, input().split()))

n1=n2=n3=n4=n5=n6=0
dx = [0,0,0,-1,1]
dy = [0,1,-1,0,0]

alst = []
for dr in lst:
    nx = x + dx[dr]
    ny = y + dy[dr]
    if 0<=nx<N and 0<=ny<M:
        if dr == 1:
            n1,n3,n4,n6 = n4, n1, n6, n3
        elif dr == 2:
            n1,n3,n4,n6 = n3, n6, n1, n4    
        elif dr == 3:
            n1,n2,n5,n6 = n5, n1, n6, n2
        elif dr == 4:
            n1,n2,n5,n6 = n2, n6, n1, n5

        if arr[nx][ny]==0:
            arr[nx][ny] = n6
        else:
            n6, arr[nx][ny] = arr[nx][ny], 0

        alst.append(n1)
        x = nx
        y = ny

print(*alst, sep='\n')
