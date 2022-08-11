# 2001_파리퇴치
# 220811

import sys
sys.stdin = open('input.txt','r')

T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    fly = []
    for _ in range(N):
        fly.append(list(map(int, input().split())))

    max_fly = 0
    for i in range(N-M+1):    # 파리채 시작점 : index 0 ~ N-M 
        for j in range(N-M+1):  
            fly_cnt = 0
            for di in range(M):   # 파리채 크기 만큼 더함
                for dj in range(M):
                    fly_cnt += fly[i+di][j+dj]
            if fly_cnt > max_fly:
                max_fly = fly_cnt

    print('#{} {}'.format(tc, max_fly))