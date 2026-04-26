def make_set(v, parent, rank):
    parent[v] = v
    rank[v] = 1

def find_set(v, parent):
    if v == parent[v]:
        return v
    
    parent[v] = find_set(parent[v], parent)
    return parent[v]

def union_sets(a, b, parent, rank):
    a = find_set(a, parent)
    b = find_set(b, parent)

    if rank[a] < rank[b]:
        a, b = b, a
    
    parent[b]=a
    if rank[a] == rank[b]:
        rank[a] += 1

# n - liczba wierzcholkow 
# E - lista krawedzi w postaci (waga, v, u),
#  wierzcholki numerowane od 0
def mst(n, E):
    parent = [-1]*n
    rank = [-1]*n

    for i in range(n):
        make_set(i, parent, rank)

    E.sort()
    mst_edges = [] # wszyskie krawedzie w mst 
    cost = 0 # koszt sumaryczny krawedzi w mst 

    for c, v, u in E:
        if find_set(v, parent) != find_set(u, parent):
            cost += c
            mst_edges.append((v, u))
            union_sets(v, u, parent, rank)

    return cost, mst_edges
