# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 13:21:34 2021

@author: LG
"""

from collections import deque

for i in graph[1]:
    print(i)



def bfs(graph, start, visited):
    # 막말로 deque이거 그렇게 막 빡세게 필요했던 거는 아님
    # 리스트에서 왼쪽꺼 못뺄 뿐이니까 popleft쫌 해줄라고 넣은
    # 새로운 함수 일 뿐..
    queue = deque([start])
    
    visited[start] = True
    
    while queue:
        #여기서 그러니까 팝 1 때리고 나중에 1노드 238이 다 빠지면 그때 다시
        #돌아와서 2를 없애는 그런식임
        # 그리고 2를 돌때 2의 노드를 없애고 나서
        # 마지막에 돌아오면 모든 노드 다 팝 때리는 구조로 만들어놓음
        v = queue.popleft() #여기서 1 팝레프트 뿌심
        print(v , end = ' ')
        
        # 그러니까 각각의 노드를 진행할때,
        for i in graph[v]:
            #만약에 이거 들린곳이 아니라면 deque리스트에 어펜드
            #deque는 그냥 리스트랑 다를것은없음
            if not visited[i]:
                #이 append는 238다 쳐넣는게 아니라 2만 하는거임
                queue.append(i)
                print(queue)
                #여기서 방문할 리스트 번호에 True넣어주는식
                visited[i] = True
                print(visited)
                
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] *9

bfs(graph, 1 , visited)


    