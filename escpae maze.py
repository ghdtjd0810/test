# -*- coding: utf-8 -*-


from collections import deque

n, m = map(int, input().split())

graph = []

for i n range(n):
    graph.append(list(map(int, input())))
    

#상하좌우 근데 잘생각해야될게, grpah[0][0] 이게 현실에서 1,1이고,
#리스트로 맵을 표현했기 때문에 가로가 x가 아니고 세로가 x임
# 그리고 x의 -1, y의 0 으로 세로로 각각 좌표를 구하는거임    
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    # 이거는 리스트 대신 그냥 deque넣은거
    queue = deque()
    #얘는 일단 pop.left한번 while안에서 해야되서 넣은거임
    queue.append((x,y))
    
    #만약에 queue에 하나도 리스트 없을때 그때 반환
    # or 마지막 행열에 도착했을때 값을 반환하면서 while문 탈피
    while queue:
        x, y = queue.popleft()
        
        #상하좌우 살펴보면서 각각 움직일 좌표 구함
        for i in range(4):
            nx = x+ dx[i]
            ny = y+ dy[i]
            
            # 만약에 -1 이나 맵튀어나가면 바로 중지
            if nx<0 or ny <0 or nx >= n or ny >= m:
                continue
            
            #그러지않고 0을 만난다면, 그러면 그만하고 올라가서 루프 돌거임
            if graph[nx][ny] == 0:
                continue
            
            # 만약에 길을 발견했다? 그러면 일단 그 좌표는 1을 더해주고, 
            # 큐 리스트에 더해줌
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] +1
                queue.append((nx,ny))
                
    return graph[n-1][m-1]

print(bfs(0,0))