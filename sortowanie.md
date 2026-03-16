# Sortowanie (Wykład 2, 11.03)
***

- Dane
    - Tablica
    - Lista
    - Plik
- Czas działania
    - proste $O(n^2)$
    - szybkie $O(n \log n)$
- Stabilnosc - Stabilny algorytm nie zamienia wzglednej pozycji elementu o tym samym kluczu
- W miejscu - algorytm uzywa tylko $O(1)$ dodatkowej pamięci

## Sortowanie przez scalanie (Merge Sort)
***

- Posortuj osobno lewą i prawą część tablicy 
- Scal w posortowaną
```python
    # A i B - dwie połówki do scalenia
    # p - miejsce gdzie zaczyna sie fragment posortowany
    # q - początek drugiej połowki (i koniec pierwszej)
    # r - koniec drugiej połowki
    def merge(A, B, p, q, r):
        i = p
        j = q
        k = p
        while i< q and j<r:
            if A[i] <= A[j]:
                B[k] = A[i]
                i+=1
            else:
                B[k] = A[j]
                j+=1
            k+=1
        
        while i<q:
            B[k]=A[i]
            i+=1
            k+=1

        while j<r:
            B[k] = A[j]
            j+=1
            k+=1
        
        for t in range(p, r):
            A[t] = B[t]
    
    # Sortujemy fragment tablicy miedzy p i r
    def merge_sort(A, B, p, r):
        if r-p > 1:
            q = (r+p)//2
            merge_sort(A, B, p, q)
            merge_sort(A, B, q, r)
            merge(A, B, p, q, r)
    
    def msort(A):
        n = len(A)
        B = [0]*n
        merge_sort(A, B, 0, n)
```
**Czas działania mergeSort** - $O(n \log n)$
**Złozonosc pamieciowa** - $O(n)$

## Sortowanie kopcowe (Heap Sort)
***
Kopiec - drzewo binarne, w którym zawartość kazdego z węzłów jest większa lub równa zawratości węzłów w jego poddrzewach.

![image info](https://www.tutorialspoint.com/data_structures_algorithms/images/min_heap_example.jpg)


**Trawersowanie po kopcu**
```python 
    # Przejście do rodzica
    def parent(i): return (i-1)//2
    # Przejście do lewego dziecka
    def left(i): return i*2+1
    # Przejście do prawego dziecka
    def right(i): return i*2 +2
```

**Zmiana zepsutego poddrzewa w kopiec**
Poddrzewo ponizej wierzchołka z indeksem i jest juz kopcem

Złozoność obliczeniowa - $O(\log n)$
```python
    def heapify(A, n, i):
        # Sprawdzamy, który element jest największy
        max_ind = i
        if left(i)<n and A[left(i)]>A[max_ind]:
            max_ind = left(i)
        if right(i)<n and A[right(i)]>A[max_ind]:
            max_ind = right(i)

        # Jeśli rodzic nie jest najwiekszym elementem, zamieniamy go z nim i sprawdzamy dalej w dół
        if max_ind != i:
            A[i], A[max_ind] = A[max_ind], A[i]
            heapify(A, n, max_ind)
```
**Budowa kopca**
$n/2 * 0 + n/4 * 1 + n/8 * 2 + ...$ - wykonanych operacji 
Złozonosc obliczeniowa budowy - $O(n)$
```python
    def build_heap(A):
        n = len(A)
        
        # Zaczynamy od dołu drzewa (pomijając liście)
        for i in range(parent(n-1), -1, -1):
            heapify(A, n, i)
``` 
**Sortowanie**
```python
    def heap_sort(A):
        build_heap(A)
        n = len(A)
        for i in range(n-1)
            #zapis niepoprawny w py, dla latwosci czytania
            swap(A[0], A[n-i-1])
            heapify(A, n-i-1, 0)
```