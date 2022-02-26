n, m = map(int, input().split())

s = []

def f():
  if len(s) == m:
    print(' '.join(map(str, s)))
    return

  for i in range(1, n + 1):
    if i in s:
      continue
    s.append(i)
    f()
    s.pop()

f()

# --------------------------------------

n,m = list(map(int,input().split()))
 
s = []
 
def dfs():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(1,n+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()
 
dfs()


# 백트래킹은 DFS(Depth-First Search, 깊이 우선 탐색)의 방식을 기반으로, 불필요한 경우를 배제하며 원하는 해답에 도달할 때까지 탐색하는 전략이다.
# DFS를 기반으로 두고 있기 때문에 스택(Stack)을 이용해 퇴각을 하며 다음 탐색을 진행하기 때문에 백트래킹(또는 퇴각검색)이라 불린다.

# 백트래킹은 기본적으로는 모든 경우의 수를 탐색한다는 브루트 포스(Brute Force) 전략을 취하지만, 처리 속도를 향상시키기 위한 가지치기(Pruning)가 중요한 역할을 한다.
# 나무에서 불필요한 가지를 제거하듯이 백트래킹에서 가지치기를 잘 할수록 불필요한 경우가 제거되어 처리 속도가 많이 향상된다.

# 참고 https://jamesu.dev/posts/2020/04/13/baekjoon-problem-solving-15649/
