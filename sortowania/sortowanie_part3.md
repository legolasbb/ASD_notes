# Sortowanie i abstrakcyjne struktury danych (Wykład 4, 25.03)
TBD - add sources and fix last picture
***
## Magiczne 5-ki 
Wybór k-tego elementu co do wielkości (k-ta statystyka pozycyjna) w czasie $O(n)$
***
Na wejściu tablica n elementów oraz k
1. Dzielimy dane na $n/5$ grup po 5 elementów
2. W kazdej grupie znajdujemy medianę
3. Znajdujemy medianę median - x (wywołanie rekurencyjne)
4. Wywołujemy partition względem pivota x
5. 
    - Jeśli t (indeks od x) = k, kończymy działanie
    - Jeśli k < t, wywołanie rekurencyjne na lewo
    - Jeśli k > t, wywołanie rekurencyjne na prawo

## Abstrakcyjne struktury danych
***
- "kontrakt" jak dane są przechowywane
    - zbiór operacji
- Fizyczna realizacja (implementacja)
    - Tablica
    - Lista
    - Struktura odsyłaczowa
    - Drzewo

#### 1. Tablica
Coś co pozwala dostać się do zawartości po indeksach/numerach
[0, 1, ..., i, ..., n-1]
#### 2. Lista jedno/dwukierunkowa
Coś co pozwalza przeglądać dane od początku do końca
(a w przypadku listy dwukierunkowej takze cofać się)
oraz **wstawiać/usuwać elementy**

[a] -> [b] -> ... -> [x] -> null

[a] <-> [b] <-> ... <-> [x] <-> null

```python
class DNode:
    def __init__(self, val):
        self.next = None
        self.prev = None
        self.val = val
```

#### Stos (stack)
Coś co pozwala na odkładnie elementów na szczyt stosu oraz ściąganie z niego

![Image info](https://media.geeksforgeeks.org/wp-content/uploads/20230116192305/stack-768.png)

***Implementacja listowa***
[top]->[]->[]
Dokładnie elementu - dodanie elementu z przodu i przesuniecie na niego wskaznika top
***Implementacja tablicowa***
[0, 1, ..., n-1]
Trzymamy liczbę elementów, nowy element dodajemy do tyłu i zwiekszamy liczbę elementów
Dwa stosy w jednej tablicy
[stos 1 ----> |     | <---- stos 2]

#### Analiza zamortyzowana rosnącego stosu
- gdy stos jest za mały to alokujemy 2x wiekszą tablicę
i tam kopiujemy jego zawrtość
- Niektóre z operacji push będą drozsze (konieczność skopiowania danych), ale rozkładając ten koszt na wszyskie operacje, średnio pojedyńczy push będzie odbywał się w czasie stałym

#### Kolejka (queue)
coś co pozwala dodać element na koniec i zabrać z początku
- Listowa 
[head]->[ ]->...->[tail]
Dokładanie elementu polega na dodaniu elementu do tyłu oraz przestawienia tail na next
Usuwanie polega na przestawieniu head na next
- Tablicowa
[1, 2, 3, 4, ...]
Dokładanie elementu
[1, 2, 3, 4, 5, ...]
Usuwanie elementu
[null, 2, 3, 4, 5, ...]
Trzymamy wskaśnik na head oraz liczbe elementow

***Zadanie*** Jak zaimplementować kolejkę mając dwa stosy, w zamortyzowanym czasie stałym?

#### Kolejka priorytetowa
coś co pozwala wkładać elementy z 'priorytetem' i wyciągać w kolejności malejących priorytetów
***Implementacje***
- Kopiec binarny
- Posortowana tablica/lista
- Nieposortowana tablica

### Tablica asosjacyjna/słownik 
Coś jak tablica, ale indeksy mogą być dowolnego typu
np. A["napis"]=17

***Implementacje***
- Tablice haszujące
- Drzewa BST (binary search tree)

Na lewo trafiają wartości mniejsze od węzła, na prawo większe
![Image info](https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Binary_search_tree.svg/250px-Binary_search_tree.svg.png)
