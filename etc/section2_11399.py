N = int(input()) # 사람수
A = list(map(int, input().split())) # 리스트
S = [0]*N  # 각 사람이 인출을 완료하는 데 필요한 시간을 저장

for i in range(1, N):
    insert_point = i  # 인덱스 값
    insert_value = A[i]
    for j in range(i-1, -1, -1):
        if A[j] < A[i]:
            insert_point = j+1
            break
        if j == 0:
            insert_point = 0

    # 한칸씩 이동하는 연산 
    for j in range(i, insert_point, -1):
        A[j] = A[j-1]
    A[insert_point] = insert_value # 삽입 위치에 현재 데이터 저장

S[0] = A[0]

# 합배열 저장
for i in range(1, N):
    S[i] = S[i-1] + A[i]

sum = 0
for i in range(0, N):
    sum += S[i]
    
print(sum)
