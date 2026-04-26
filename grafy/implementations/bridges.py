def find_bridges(adj):
    n = len(adj)
    timer = 0
    visited = [False] * n
    tin = [-1] * n
    low = [-1] * n
    bridges = []


    def dfs(v, p=-1):
        nonlocal timer, visited, tin, low, bridges
        visited[v] = True
        tin[v] = timer
        low[v] = timer
        timer+=1
        parent_skipped = False # Potrzebne tylko dla grafow z multi-krawedziami

        for u in adj[v]:
            if u == p and not parent_skipped:
                parent_skipped = True
                continue

            if visited[u]:
                low[v] = min(low[v], tin[u])
            else:
                dfs(u, v)
                low[v] = min(low[v], low[u])
                if low[u] == tin[u]:
                    bridges.append((v, u)) 

    for v in range(n):
        if not visited[v]:
            dfs(v)
