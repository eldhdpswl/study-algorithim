# 다익스트라 문제
import sys
input = sys.stdin.readline
from queue import PriorityQueue

V, E = map(int, input().split())
K = int(input())
distance = [sys.maxsize] * (V+1)
visited = [False] * (V+1)
myList = [[] for _ in range(V+1)]
q = PriorityQueue()


# 인접리스트 정리
for _ in range(E):
    u, v, w = map(int, input().split())
    myList[u].append((v, w))


q.put((0, K))  # 거리기준으로 정렬하기 위해 0을 넣음. (거리, 노드)
distance[K] = 0

while q.qsize() > 0:
    current = q.get()  # 현재 노드
    c_v = current[1]   # 현재 노드의 목표 노드
    if visited[c_v]:
        continue
    visited[c_v] = True
    for tmp in myList[c_v]:
        next = tmp[0]  # 다음노드
        value = tmp[1]  # 가중치
        if distance[next] > distance[c_v] + value:
            distance[next] = distance[c_v] + value
            q.put((distance[next], next))


for i in range(1, V+1):
    if visited[i]: # 방문한 노드
        print(distance[i])
    else:  # 아니면
        print("INF")
      
