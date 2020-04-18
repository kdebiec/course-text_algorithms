# Zad 6

## Algorytm nawiny działa najwolniej w momencie kiedy ma zadany długi
## wzorzec, którego większa część początkowa znajduje się w większości tekstu

## Przykład
import time

from automata import transition_function, fa_string_matching
from kmp import kmp, prefix_function
from naive import naive_algorithm


def testAlgorithm(text, pattern, algorithm):
    start = time.time()
    algorithm(text, pattern)
    end = time.time()
    print(end - start)


text = 'ab'*100000
pattern = 'ab' * 50000 + 'ba'

print('Naive Search')
testAlgorithm(text, pattern, naive_algorithm)

print('Finite Automata String Matching')
testAlgorithm(text, pattern, fa_string_matching)

print('KMP')
testAlgorithm(text, pattern, kmp)

# Zad 7
## Budowanie tabeli przejść działa najwolniej dla długich wzorców z rozbudowanym alfabetem

pattern = 'Pójdźże, kiń tę chmurność w głąb flaszy!'


start = time.time()
prefix_function(pattern)
end = time.time()
print("KMP prefix function:" + str(end - start))

start = time.time()
transition_function(pattern)
end = time.time()
print("Automata's transition function:" + str(end - start))