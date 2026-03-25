# Sortowanie cz. 2 (Wykład 3, 18.03)

## Quick Sort
***

Dzielnie tablicy, a nastepnie sortowanie podzielonych części

```python
    def partition(A, p, r):
        x = A[r]
        i = p-1
        for j in range(p, r+1):
            #[   | <=x | > x | j | x ]
            if A[j]<=x:
                i += 1
                swap(A[i], A[j])

        # Po wykonaniu petli - [   | <=x | x | >x   ]
        # Zwracamy indeks, pod którym znajduje się x
        return i

    # A - tablica do posortowania
    # p - poczatek fragmentu do posortowania
    # r - koniec fragmentu do posortowania (włącznie)
    def qsort(A, p, r):
        if p < r:
            # Dzielimy tablice
            q = partition(A, p, r)
            # Sortujemy rekurencyjnie podzielone części
            qsort(A, p, q-1)
            qsort(A, q+1, r)
```
Złozoność czasowa Quick Sort
- $O(n \log n)$ - Pod warunkiem idealnych podziałów
- $O(n^2)$ - Przy niekorzystnym wybraniu podziałów

Jeśli co drugi podział byłby idelany to dalej zachowamy złozoność $O(n \log n)$

### Optymalizacja funkcji qsort

```python
def qsort(A, p, r):
    while p < r:
        q = partition(A, p, r)
        qsort(A, p, q-1)
        p = q+1
```

# Sortowaania liniowe
***
## Sortowanie przez zliczanie
***
Zliczamy ile elementów o danej wartosci istnieje, a następnie z tablicy zliczonych wartosci 
tworzymy sumę prefiksową. Prefiks wykorzysujemy do stworzenia posortowanej tablicy

```python 
    # m - maksymalna wartość w tablicy
    def counting_sort(A, m)
        n = len(A)
        B = [0]*n
        C = [0]*m
        for i in range(n):
            C[A[i]]+=1
        
        for i in range(1, m):
            C[i]+=C[i-1]
        
        for i in range(n-1, -1, -1):
            C[A[i]]-=1
            B[C[A[i]]] = A[i]
        
        return B
        
```

## Radix Sort / Sortowanie pozycyjne
***
Sortujemy kolejno po cyfrach/znakach porównując od najmniej do najbardziej znaczącej cyfry/znaku
Najczęściej uzywane do sortowania ciagów znaków
Mozna równiez posortować liczby z przedziały 0, ..., n-1 w czasie $O(n \log n)$

Implementacja dla ciagow malych liter alfabetu angielskiego (a-z)

```python

    

    # counting sort jak wyzej, zmodyfikowany dla stringow
    def counting_sort(A, ind):
        def char_idx(el):
            if len(el) <= ind:
                idx = 0
            else:
                idx = ord(el[ind]) - ord('a') + 1
            
            return idx
        n = len(A)
        # Alfabet angielski ma 26 liter, jeden dodakowy gdy brak znaku
        count = [0] * 27
        output = [""] * n

        for el in A:
            idx = char_idx(el)
            count[char_idx]+=1
        
        for i in range(1, 27):
            count[i]+=count[i-1]:

        for i in range(n-1, -1, -1):
            idx = char_idx(el)
            count[idx]-=1
            output[count[idx]] = A[i]
        
        for i in range(n):
            A[i] = output[i]

        
    
    def radix_sort(A):
        # Znajdujemy najwiekszą liczbe, aby znac ilość cyfr
        m = len(max(A, key=len))

        for i in range(m-1, -1, -1):
            # Sortujemy po kolei po kazdym znaku
            counting_sort(A, i)




```

## Bucket sort / Sortowanie kubelkowe
***
Sortujemy liczby z przedziału [0, 1) wygenerowane losowo, z rozkładu jednostajnego
n - liczb
kubełki - [0, 1/n), [1/n, 2/n), ..., [n-1/n, 1)
Rozdzielamy liczby do kubełków, do których przynalezą 

Implementacja w rozwiązaniu zadania ponizej

***
**Zadanie**: Znaleźć takie duze liczby A[i], A[j], ze po posortowaniu były by obok siebie, 
ale |A[i] - A[j]| jest maksymalna.

**Rozwiązanie**: Tworzymy n+1 równych kubełkow, pierwszy zaczynający się od minimalnej wartości w tablicy, 
a ostatni kończący się na największej wartości w tablicy. Mamy n liczb i n+1 kubełkow więc z ZSD wiemy, 
ze co najmniej jeden kubełek będzie pusty. W dodatku wiemy, ze pustym kubelkiem nie bedzie zaden z skrajnych.
Stąd wiemy, ze istnieja co najmniej dwie liczby miedzy, którymi odległość bedzie długości co najmniej jednego kubełka,
więc dwie liczby wewnątrz kubełka nie mogą tworzyć najwiekszej róznicy. Teraz starczy,
ze bedziemy porownywac najmniejsza i najwieksza wartosc z sasiednich kubelkow (pomijajac puste).

Kod [tutaj](solved/bucket.py)

## Statystyki pozycyjne
***
Mamy tablice liczb A
**Zadanie**: Oblicz, która z liczb z A byłaby na pozycji k po posortowaniu
Uzywamy fukcji partition z quicksort

- Jeśli q = k (q to nasz środek podziału) jest równe  -> wynikem jest x
- Jeśli k < q to wywołujemy się na lewej części tablicy (tam gdzie elementy <=x)
- Jeśli k > q to wywołujemy się na prawej części 