import heapq

def dijkstra(graph, start):
    heap = [(0, start)]
    dist = {start: 0}
    
    while heap:
        cost, node = heapq.heappop(heap)
        if cost > dist.get(node, float('inf')):
            continue
        for neighbor, weight in graph[node]:
            new_cost = cost + weight
            if new_cost < dist.get(neighbor, float('inf')):
                dist[neighbor] = new_cost
                heapq.heappush(heap, (new_cost, neighbor))
    return dist

def dijkstra(graph, start):
    heap = [(0, start)]
    dist = {start: 0}

    while heap:
        cost, node =  heapq.heappop(heap)
        if cost > dist.get(node, float('inf')):
            continue
        for neighbor, weight in graph[node]:
            new_cost = cost + weight
            if new_cost < dist.get(node, float('inf')):
                dist[neighbor] = new_cost
                heapq.heappush(heap, (new_cost, neighbor))

    return dist
