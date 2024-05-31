import sys

input = sys.stdin.readline

n, m = map(int, input().split())

A = list(map(int, input().split()))  #원본 수열
S = [0] * n   #합배열
C = [0] * m   #같은 나머지 인덱스 카운트
answer = 0    #정답변수

S[0] = A[0]
for i in range(1, n):
    S[i] = S[i-1] + A[i]

for i in range(n):
    remainder = S[i] % m
    if remainder == 0:
        answer += 1
    C[remainder] += 1    # 변경된 합배열에서 같은 값 추가하기

for i in range(m):
    if C[i] > 1:
        answer += (C[i]*(C[i]-1) // 2) # 조합 구하는 공식

print(answer) 
