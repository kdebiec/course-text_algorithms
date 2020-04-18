import time

from automata import fa_string_matching
from kmp import kmp
from naive import naive_algorithm


def testAlgorithm(document_name, pattern, algorithm):
    with open(document_name, encoding="utf-8") as f:
        text = f.read()
        start = time.time()
        algorithm(text, pattern)
        end = time.time()
        print(end - start)


print("Time mesuring of matching 'art'")

print('Naive Search')
testAlgorithm('tests/1997_714.txt', 'art', naive_algorithm)

print('Finite Automata String Matching')
testAlgorithm('tests/1997_714.txt', 'art', fa_string_matching)

print('KMP')
testAlgorithm('tests/1997_714.txt', 'art', kmp)

############################################
print("Time mesuring of matching 'kruszwil'")

print('Naive Search')
testAlgorithm('tests/wikipedia-tail-kruszwil.txt', 'kruszwil', naive_algorithm)

print('Finite Automata String Matching')
testAlgorithm('tests/wikipedia-tail-kruszwil.txt', 'kruszwil', fa_string_matching)

print('KMP')
testAlgorithm('tests/wikipedia-tail-kruszwil.txt', 'kruszwil', kmp)