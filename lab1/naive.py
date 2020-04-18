def naive_algorithm(text, pattern):
    shifts = []
    for k in range(len(text) - len(pattern) + 1):
        if pattern == text[k:k+len(pattern)]:
            #print("wzorzec znaleziony z przesunięciem: " + str(k))
            shifts.append(k)

    return shifts

'''
naive_algorithm("cd", "abcd")
naive_algorithm("asas", "asasasasas")
f = open("tests/1997_714.txt", "r")

for line in f:
    naive_algorithm("art", str(line))
'''
