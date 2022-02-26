dx = [0,0,-1,1]
dy = [1,-1,0,0]
n,m,x,y,l = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
dice = [0]*7
move = list(map(int,input().split()))
for k in move:
    k -= 1  # 방향 배열에 넣기 위해 - 1을 하는거같다. 확인필요?
    nx,ny = x+dx[k],y+dy[k]
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        # 바깥으로 이동시키려고 하는 경우에는 해당 명령을 무시해야 함, 출력도 하면 안됨
        continue
    if k == 0:  # right
        temp = dice[1]
        dice[1] = dice[4]
        dice[4] = dice[6]
        dice[6] = dice[3]
        dice[3] = temp
    elif k == 1:  # left
        temp = dice[1]
        dice[1] = dice[3]
        dice[3] = dice[6]
        dice[6] = dice[4]
        dice[4] = temp
    elif k == 2:  # up
        temp = dice[1]
        dice[1] = dice[5]
        dice[5] = dice[6]
        dice[6] = dice[2]
        dice[2] = temp
    else:   # down
        temp = dice[1]
        dice[1] = dice[2]
        dice[2] = dice[6]
        dice[6] = dice[5]
        dice[5] = temp
    x,y = nx,ny
    if a[x][y] == 0:
        # 주사위를 굴렸을 때, 이동한 칸에 써 있는 수가 0이면, 주사위의 바닥면에 써 있는 수가 칸에 복사됨
        a[x][y] = dice[6]
    else:
        #  0이 아닌 경우에는 칸에 써 있는 수가 주사위의 바닥면으로 복사되며,
        dice[6] = a[x][y]
        #  칸에 써 있는 수는 0이 복사됨
        a[x][y] = 0
    print(dice[1])
