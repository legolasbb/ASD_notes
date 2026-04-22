from queue import PriorityQueue

class Edge:
    def __init__(self, u, d):
        self.node = u
        self.d =  d
    def __lt__(self, other):
        return self.d < other.d
    
def dijkstra(start: int, adj: list):
    n = len(adj)
    cost = [float('inf')]*n
    # Na podstawie tablicy parent mozemy odtworzyc najktrotsza sciezke
    parent = [-1]*n
    # cost[i] - koszt minimalnej ściezki od start do i
    cost[start]=0

    node_q = PriorityQueue()
    node_q.put(Edge(start, 0))

    while not node_q.empty():
        v = node_q.get()

        if v.d != cost[v.node]:
            continue

        for u in adj[v.node]:
            if cost[v.node] + u.d < cost[u.node]:
                cost[u.node] = cost[v.node] + u.d
                parent[u.node] = v.node
                node_q.put(Edge(u.node, cost[u.node]))