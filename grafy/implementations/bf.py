#Bellman-Ford
class Edge:
    def __init__(self, v, u, cost):
        self.v = v
        self.u = u
        self.cost = cost

def bf(n, m, edges, s):
    d = [float('inf')] * n
    d[s] = 0
    p = [-1] * n
    x = -1
    
    for i in range(n):
        x = -1
        for e in edges:
            if d[e.v] != float('inf'):
                if d[e.u] > d[e.v] + e.cost:
                    d[e.u] = d[e.v] + e.cost  
                    p[e.u] = e.v              
                    x = e.u                   
    
    if x == -1:
        return None
    
    y = x
    for i in range(n):
        y = p[y]

    path = []
    cur = y
    while True:
        path.append(cur)
        if cur == y and len(path) > 1:
            break
        cur = p[cur]
        
    path = path[::-1]
    return path