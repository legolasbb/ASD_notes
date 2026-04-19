def dfs(v: int, adj: list, output: list, visited: list)->None:
    visited[v] = True
    for u in adj[v]:
        if not visited[u]:
            dfs(u, adj, output, visited)
    
    output.append(v)

# Adj - lista sasiedztwa grafu skierowanego (wiercholki numerowane od 0)
# Zwraca liste list, zawierajacych silnie spojne skladowe
def strongly_connected_components(adj: list)->list:
    n = len(adj)
    order = []
    visited = [False]*n

    for i in range(n):
        if not visited[i]:
            dfs(i, adj, order, visited)

    adj_rev = [[] for _ in range(n)]
    for i in range(n):
        for v in adj[i]:
            adj_rev[v].append(i)

    visited = [False]*n
    components = []
    order = order[::-1]

    for v in order:
        if not visited[v]:
            component = []
            dfs(v, adj_rev, component, visited)
            components.append(component)
    
    return components
