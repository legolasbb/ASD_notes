# Algorytmy Grafowe (Wykład 6, 08.04)

## Sortowanie topologiczne
***
G = (V, E) - graf skierowany<br>
dag - skierowany graf acykliczny<br>
W zadaniu sortowania topologicznego mamy dany dag i szukamy takiej kolejności, że każda krawędź
prowadzi z "lewej na prawą".

**Przebieg sortowania**
- Wykonuj DFS
- W momencie przetworzenia wierzchołka, dopisz go na początek tworzonej kolejności

## Cykl Eulera
***
***Tw.***<br>
Graf nieskierowany ma cykl Eulera wtw. jest spójny i każdy wierzchołek ma stopień parzysty<br>
**Znajdowanie cyklu Eulera**
- Wykonuj DFS usuwając odwiedzone krawędzie
- W momencie przetworzenia (tzn. wszyskie krawędzie z wierzchołka zostały już usunięte) wierzchołka dopisz go na początku cyklu

G - graf reprezentowany listowo, mający cykl Eulera<br>
G[v] - lista wierzchołków, do których jest krawędź v, **posortowana rosnąco**
```python
def euler(G):
    n = len(G)
    idx = [0 for _ in range(n)]
    cycle = []
    def dfs_visit(v):
        nonlocal G, idx, cycle
        while idx[v]<len(G[v]):
            u = G[v][idx[v]]
            idx[v]+=1
            if idx[u]>=len(G[u]) or G[u][idx[u]]>v:
                continue
            dfs_visit(u)
        cycle.append(v)
    dfs_visit(0)
    return cycle
```
## Silnie spójne składowe
***
Mówimy, że wierzchołki u,v grafu skierowanego G należą do tej samej silnie spójnej składowej
jeśli istnieje ścieżka skierowana z u do v oraz ścieżka skierowana z v do u.<br>
**Algorytm**
- Uruchom DFS zapisując czasy przetworzenia
- Odwróć kierunek wszystkich krawędzi 
- Wykonaj DFS ponownie w kolejności malejących czasów przetworzenia
##  Mosty w grafach
Most jest krawędzia, której usunięcie rospójnia graf.<br>
**Algorytm znajdywania mostów**
- Wykonaj DFS zapisując czasy odwiedzenia wierzchołków
- Dla każdego wierzchołka oblicz ***low(v)=min( d(v), min{ d(u) | u jest osiągalny krawędzią wsteczną z v }, min{ low(w) | w jest dzieckiem v w drzewie DFS})***
- Krawędź {parent(v), v} jest mostem gdy low(v)=d(v) 