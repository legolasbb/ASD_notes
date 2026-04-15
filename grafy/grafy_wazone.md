# Grafy ważone / najkrótsza ścieżka (Wykład 7, 15.04)
***
## Reprezetacja grafu
***
G = (V, E) - graf skierowany lub nie<br>
$$w: E \to \mathbb{N}(\mathbb{Q}, \mathbb{Z})$$
**W reprezentacji macierzowej**:<br> $W[i][j] = w(v_i, v_j)$<br>
Jeśli danej krawędzi nie ma to np. $W[i][j] = \infty$<br><br>
**W reprezentacji listowej**<br>
$[v_1] \to [v_2, 7] \to  [v_7, 5]$<br>
$[v_2] \to [v_4, 1]$ itd.
## Problem najkrótszych ścieżek
***
- 1-1 - szukamy ścieżki najkrótszej z s do t
- 1-wszyscy - szykamy ścieżek z $s \in V$ do wszyskich innych wierzchołków
- wszyscy-wszyscy - szukamy ścieżek między każdą parą wierzchołków 
## Algorytm Dijkstry
***
Wykonujemy algorytm BFS ze sztucznymi wierzchołkami, 
ale zawsze od razu zajmujemy się najbliższym prawdziwym wierzchołkiem.<br><br>
Dla każdego wierzchołka $ v \in V$: 
- $v.d$ = oszacowanie odległości z s 
(wierzchołek startowy) do v
- $v.parent$ = aktualny poprzednik na ścieżce z s do v
### Algorytm (szykamy ścieżek z $s \in V$)
1. Dla każdego wierzchołka $v \in V$ ustaw $v.d = \infty$. 
Umieść wszyskie wierzchołki w kolejce priorytetowej Q (typu min, v.d jako klucz)
2. $s.d = 0$; aktualizacja kolejki
3. Dopóki Q nie jest pusta:<br>
u = wierzchołek wyciągniety z kolejki, dla kazdej krawedzi (u, v) wykonaj:
   - jeśli  $u.d + w(u,v) < v.d$ to:<br>
       $v.d = u.d + w(u, v)$<br>
       $v.parent=u$<br>

**Złożoność czasowa** - $O(E \log V)$

![Image info](https://upload.wikimedia.org/wikipedia/commons/5/57/Dijkstra_Animation.gif)
<br>
**W implementacji należy pominąć dodawanie wszyskich wierzchołków do kolejki w kroku 1.**<br>
**W dodatku do $v.d = u.d + w(u, v)$ dodajemy ten wierzchołek podwownie z zmniejszoną wartością**
## Algorytm Bellmana-Forda
#### (Dopuszcza wagi ujemne)
***
Jeśli dopuszczamy wagi ujemne to musimy ograniczyć się do grafów skierowanych, ponieważ
w grafie nieskierowanym każda krawędz o ujemnej wadze tworzy cykl o ujemnej wadze.
### Algorytm
1. Inicjalizacja tak samo jak w algorytmie Dijkstry, ale bez kolejki.
2. for i in range($|V|-1$):<br>
    &emsp; &emsp;for $e=(u,v) \in E$: Wykonaj relaksacje $(u,v)$
3. Weryfikacja:<br>
Dla każdej krawędzi $(u, v) \in E$ sprawdzamy: $v.d \le u.d + w(u, v)$<br>
Jeśli dla któreść nie zachodzi to mamy cykl o ujemnych wartościach.<br>
**Złożoność czasowa** - $O(E*V)$
