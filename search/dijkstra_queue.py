import heapq
from search.errors import PathNotFound, VertexNotFound


def search(graph: dict, start, stop):
    """Dijkstra with priority queue"""
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    parents = {vertex: None for vertex in graph}
    pointer = stop
    path = []

    if start not in graph:
        raise VertexNotFound(start)
    elif stop not in graph:
        raise VertexNotFound(stop)

    priority_queue = [(0, start)]
    while len(priority_queue) > 0:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbour, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbour]:
                distances[neighbour] = distance
                heapq.heappush(priority_queue, (distance, neighbour))
                parents[neighbour] = current_vertex

    while pointer is not None:
        path.append(pointer)
        pointer = parents[pointer]

    if distances[stop] == float('infinity'):
        raise PathNotFound(stop)

    # print(distances)
    path.reverse()
    return path
