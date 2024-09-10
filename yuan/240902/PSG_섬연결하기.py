'''
모의고사 문제 1
삼각형의 사이클 여부 확인하는 prim's 알고리즘 
heapq에 거리,노드를 넣고
갈수 있는 노드 기준 가장 짧은 거리 &방문처리 해서 
최소신장트리 구현 가능함 
'''



import heapq

def solution(n, costs):

#     n은 섬개수 graph 는 섬간의 관계표현 
    graph = [ [] for _ in range(n) ]
    link_num = len(costs)
    pq = []

    for i in range(link_num):
        a = costs[i][0]
        b = costs[i][1]
        c = costs[i][2]
        graph[a].append([b,c])
        graph[b].append([a,c])
    
    now = 0
    for go in graph[now]:
        nxt = go[0]
        cst = go[1] 
        heapq.heappush(pq,[cst,nxt])
    
    visited = [False for _ in range(n)]
    visited[now]  = True 
    total = 0
    
    while pq:
        # 꺼내기
        cst, nxt = heapq.heappop(pq)         
        if visited[nxt]:
            continue
            
        total +=cst
        visited[nxt] = True
        
        # 현재에서 갈수 있는 다음 노드 넣기
        for nxxt in graph[nxt]:
            if not visited[nxxt[0]]:
                heapq.heappush(pq,[nxxt[1], nxxt[0]])

 
    return total