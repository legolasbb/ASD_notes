# Wykład 6 (29.04)
## Metody konstruowania algorytmów
***
- metoda dziel i  zwyciężaj
- programowanie dynamiczne
- algorytmy zachłanne
### Obliczanie n-tej liczby Fibonacciego 
$F_0 = 1$<br>
$F_1 = 1$
$F_n = F_{n-1} + F_{n-2}, n\ge2$

```python
def fib_dp(n):
    F = [1]*(n+1)
    for i in range(2, n+1):
        F[i] = F[i-1] + F[i-2]
    return F[n]
```
Złożoność - $O(n)$

## Problem najdłuższego rosnącego podciągu (lis)
***
Dane: Tablica A zawierająca n liczb
Zadanie: znależź podciąg rosnący o maksymalnej długości, niekoniecznie spójny

I. Wymyślamy funkcję, którą będziemy obliczać, która pomoże znaleźć rozwiazanie

f(k) - długość najdłuższego podciągu kończącego się na A[k]<br>
złe: g(k) = długość najdłuższego podciągu dla A[0], ..., A[k]<br>

II. Wyznaczanie wzoru rekurencyjnego na f<br>
```math
f(k) = \max \{ 1 + f(i) \mid i < k \land A[i] < A[k] \}
```
III. 
```python
def lis(A):
    n = len(A)
    F = [1]*n
    for k in range(1, n):
        for i in range(k):
            if A[i] < A[k] and F[k] < F[i]+1:
                F[k] = F[i]+1
    
    return  max(F)
```

## Problem zboru wierzchołków niezależnych na drzewie (IS):
Szukamy zbioru wierzchołków niezależnych o maksymalnej sumie wartości 
I. Funkcje, które obliczamy
f(v) = wartość najlepszego rozwiązania dla poddrzewa ukorzenionego w v
g(v) = wartość najlepszego rozwiązania dla poddrzewa ukorzenionego w v, które nie zawiera v
II. Zapis rekurencyjny

$g(v) = \sum\limits_{u_i \in dzieci} g(u_i)$
$f(v) = max(g(v), fun(v) + \sum\limits_{u_i \in dzieci} g(u_i)$

```python
class Node:
    def __init__(self, fun):
        self.fun = fun
        self.children = []
        self.f = -1
        self.g = -1
    def comp_f(self):
        if self.f != -1: return self.f
        val = self.fun
        for u in children:
            val += u.comp_g()
        self.f = max(self.comp_g(), val)
        return self.f
    def comp_g(self):
        if self.g != -1: return self.g
        self.g = 0
        for u in children:
            self.g += u.comp_f()
        return self.g
```
