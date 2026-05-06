# Wykład 7 (06.05)
## Problem plecakowy (dyskretny)
***
Dane: I = {0, 1, ..., n-1} - zbiør przedmiotów<br>
P: $I \to \mathbb{N}$ - ceny przedmiotów<br>
W: $I \to \mathbb{N}$ - wagi przedmiotów<br>
$B \in \mathbb{N}$ - ile mozna unieść
Zadanie znalezc podzbiór J zawierajacy sie w  I, który maksymalizuje<br>
$P(J) = \sum\limits_{i \in J} P(i)$<br>
pod warunkiem:<br>
$W(J) = \sum\limits_{i \in J} W(i) \le B$<br>
#### I. Funkcja, która obliczamy<br>
f(i, b) = największa wartość przedmiotów spośród {0, ..., i}, których łączna waga nie przekracza B<br>
Wynik f(n-1, B)<br>
####  II. Sformułowanie rekurencyjne<br>
$f(0, b) = P(0),  b \ge W(0)$; inaczej 0<br>
$f(i, b) = max(f(i-1, b), f(i-1, b - W(i)) + P(i))$<br>
#### III. Implementacja 
```python
def knapsack(P, W, B):
    n = len(P)
    F = [[0]*(B+1) for _ in range(n)]
    for b in range(W[0], B+1):
        F[0][b] = P[0]
    for i in range(1, n):
        for b in range(B+1):
            F[i][b] = F[i-1, b]
            if b >= W[i]:
                F[i][b] = max(F[i][b], F[i-1][b-W[i]] + P[i])
    
    return F[n-1][B]
```
## Problem komiwojażera (TSP)
***
**Dane:<br>**
$C = \{1, .., n\}$<br>
d: $C * C \to \mathbb{N}$ - odległość między miastami<br>
**Zadanie:<br>**
Znaleźć taką trasę komiwojażera, 
która każde miasto odwiedza raz (zaczynamy i kończymy w tym samym miejscu)
i której suma odległości jest minimalną<br><br>
#### I. Funckcja<br>
$S \subseteq C, t \in S, 1 \in S$<br>
$f(S, t) = $ najktótsza ścieżka z 1 do t, zawierająca wszystkie miasta z S
<br>
**Wynik:** $min(f(C, t) + d(t, 1)), t \in C$<br>
#### II. Rekurencja<br>
$f(\{1\}, 1) = 0$
$f(S, t) = min(f(S / \{t\}) + d(r, t)), r \in S / \{t\}$<br>
Złożoność czasowa - $O(2^n * n^2)$
## Bitoniczny TSP
***
Miasta to punkty w $\mathbb{R}^2$<br>
Trasa najpierw przebiega tylko w lewo, potem tylko w prawo
(dla ułatwienia, każdy punkt ma inną współrzędną x).<br>
$x_1, ..., x_n$ - kolejne miasta, posortowane według wspólrzędnej x
<br><br>
#### I. Funkcja
$f(x_i, x_j) = $ najmiejsza suma długości dwóch tras z $x_1$, z których pierwsza dochodzi do $x_i$,
druga do $x_j$ i używają miast $x_1, ..., x_j$<br>
Wynik: $min(f(x_i, x_n) + d(x_i, x_n)), x_i \in C$
#### II. Rekurencja
##### a)
$i < j-1$<br>
$f(x_i, x_j) = f(x_i, x_{j-1}) + d(x_{j-1}, x_j)$
##### b)
$f(x_{j-1}, x_j) = min(f(x_k, x_{j-1}) + d(x_k, x_j)), k < j-1$
#### Implementacja
D = tablica z odległościami
```python
F = [[float('inf')]*n for _ in range(n)]
F[0][1] = D[0][1]

def f(i, j, F, D):
    if F[i][j] != float('inf'): return F[i][j]
    if i < j-1:
        F[i][j] = f(i, j-1, F, D) + D[j-1][j]
    else:
        for k in range(j-1):
            F[i][j] = min(F[i][j], f(k, j-1, F, D) + D[k][j])
    
    return F[i][j]
```
**Złożoność czasowa** - $O(n^2 * n) = O(n^3)$
