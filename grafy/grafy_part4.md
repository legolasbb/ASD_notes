# Najkrótsze ścieżki między każdą parą wierchołków
***
### Podejścia proste

- |V| wywołań algorytmu Dijkstry $O(VE \log V)$
- |V| wywołań algorytmu B-F $O(V^2E)$

Speccjalizowane algorytmy działają w reprezentacji macierzowej
Szukając:
- D[u][v] - najkrótszej ścieżki z u do v
- P[u][v] - poprzednik v na najkrótszej ścieżce z u do v

### Idea algorytmu Floyda-Warshalla

$V = \{ v_1, v_2, ..., v_n\}$ - wszystkie wierzchołki
Znamy najkrótsze ścieżki między każda parą wierzchołków, używające 
$\{ v_1, v_2, ..., v_{k-1}\}$. Na tej podstawie znaduje najkrótsze ścieżki
z $\{ v_1, v_2, ..., v_k\}$ jako wierzchołek wewnętrzny.
 
D(k) - macierz długości najkrótszych ścieżek używających wewnetrznie $\{ v_1, v_2, ..., v_k\}$

```python
def FW(D):
    for k in range(1, n):
        for u in V:
            for v in V:
                D[u][v] = min(D[u][v], D[u][k] + D[k][v])
```