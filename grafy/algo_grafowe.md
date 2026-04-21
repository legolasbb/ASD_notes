# Algorytmy Grafowe (Wykład 5, 01.04)

## Reprezentacja grafu
***
![image info](https://www.flynerd.pl/wp-content/uploads/2018/10/graf-skierowany-4-wierzcholki.png)<br>
(Reprezentacje dla grafu powyzej)
### 1. Lista krawedzi
[(1, 2), (1, 3), (1, 4), (2, 4), (3, 4)]
### 2. Reprezetacja macierzowa
Tablica n x n gdzie n to liczba wierzchołków. Jesli miedzy wierzchołkiem v i w jest krawedź to tab[v][w] = True
### 3. Listy sąsiadów
W tab[i] mamy liste wierzcholkow, do których wychodzi krawędz z i-tego wierzchołka

[<br>
1: [2, 3, 4]<br>
2: [4]<br>
3: [4]<br>
4: []<br>
]

# Przeszukiwanie grafu
## BFS (Breadth-First Search, przeszukiwanie wszerz)
***
![image info](https://upload.wikimedia.org/wikipedia/commons/5/5d/Breadth-First-Search-Algorithm.gif?_=20100504223639)
```python
    def BFS(G: List, s: int)->None:
        n = len(G)
        next  = deque()
        visited = [False]*n
        
        next.append(s)
        visited[s]=True
        
        while len(next):
            # Usuwa wierzcholek z lewej strony
            v = next.popleft()
            # Wyswietlamy wierzcholki, które odwiedzamy
            print(v)
            for u in G[v]:
                if not visited[u]:
                    # Dodaje wierzchołek na prawa strone kolejki
                    next.append(u)
                    visited[u]=True

```
## DFS (Depth-First Search, przeszukiwanie wgłab)
***
![image info](https://upload.wikimedia.org/wikipedia/commons/7/7f/Depth-First-Search.gif?_=20090326120256)
```python
    def DFS(G: list, s: int)->None:
        n = len(G)
        next = deque()
        visited = [False]*n
        
        deque.append(s)
        visited[s]=True
        
        while len(next):
            # Usuwamy element z gory
            v = next.pop()
            print(v)
            for u in G[v]:
                if not visited[u]:
                    # Dodajemy wierzcholek na gore stosu
                    next.append(u)
                    visited[u]=True
        
```