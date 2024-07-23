# 퇴사

import sys
inpuut = sys.stdin.readline

def dfs(n, sm):
    global ans
    if n == N:
        ans = max(ans, sm)
        return
    
    if n+T[n]  <= N:
        dfs(n+T[n], sm+P[n])

    dfs(n+1, sm)    

N = int(input())
T = [0]*N
P = [0]*N
  
for i in range(N):
    T[i], P[i] = map(int, input().split())

ans = 0
dfs(0, 0)

print(ans)
