from search.errors import PathNotFound, VertexNotFound


def search(graph, start, stop):
    """A*"""
    open_list = set(start)
    closed_list = set()
    distances = {start: 0}
    parents = {start: start}
    heuristics = {vertex: 1 for vertex in graph}  # not implemented

    if start not in graph:
        raise VertexNotFound(start)
    elif stop not in graph:
        raise VertexNotFound(stop)

    while len(open_list) > 0:
        n = None

        for vertex in open_list:
            # if n is None or distances[vertex] + heuristics[vertex] < distances[n] + heuristics[n]:
            if n is None or distances[vertex] < distances[n]:
                n = vertex

        if n == stop:
            path = []

            while parents[n] != n:
                path.append(n)
                n = parents[n]

            path.append(start)
            path.reverse()
            # print(distances)
            return path

        for m, weight in graph[n].items():
            if m not in open_list and m not in closed_list:
                open_list.add(m)
                parents[m] = n
                distances[m] = distances[n] + weight
            else:
                if distances[m] > distances[n] + weight:
                    distances[m] = distances[n] + weight
                    parents[m] = n

                    if m in closed_list:
                        closed_list.remove(m)
                        open_list.add(m)

        open_list.remove(n)
        closed_list.add(n)

    raise PathNotFound(stop)
