# 백준 15662 톱니바퀴(2)

n = int(input())
a = [list(input()) for _ in range(n)]
k = int(input())
for _ in range(k):
    no,dir = map(int,input().split())
    no -= 1
    d = [0]*n
    d[no] = dir
    
    # 각각의 톱니는 동시에 회전해야 하기 때문에
    # 먼저, 각 톱니가 어떤 방향으로 회전해야 하는지 구하자

    # 왼쪽 톱니를 연쇄적으로 구하고
    for i in range(no-1, -1, -1):
        if a[i][2] != a[i+1][6]:  # 하나의 톱니바퀴를 기준으로 오른쪽을 체크
            d[i] = -d[i+1]
        else:
            # 한 톱니가 회전하지 않으면
            # 그 톱니의 왼쪽에 있는 톱니도 회전하지 않는다.
            break

    # 오른쪽 톱니를 연쇄적으로 구하고   
    for i in range(no+1, n):
        if a[i-1][2] != a[i][6]:  # 하나의 톱니바퀴를 기준으로 왼쪽을 체크
            d[i] = -d[i-1]
        else:
            # 한 톱니가 회전하지 않으면
            # 그 톱니의 왼쪽에 있는 톱니도 회전하지 않는다.
            break
    
    # 조사    
    for i in range(n):
        if d[i] == 0:
            continue

        # 시계 방향 회전
        if d[i] == 1:
            temp = a[i][7]
            for j in range(7, 0, -1):
                a[i][j] = a[i][j-1]
            a[i][0] = temp

        # 반시계 방향 회전    
        elif d[i] == -1:
            temp = a[i][0]
            for j in range(0, 7):
                a[i][j] = a[i][j+1]
            a[i][7] = temp
ans = 0
for i in range(n):
    if a[i][0] == '1':  #12시 방향 S극
        ans += 1
print(ans)
