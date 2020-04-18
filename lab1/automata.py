def transition_function(pattern):
    alphabet_symbols = set(pattern)
    transition_table = []
    lps = 0

    for i in range(0, len(pattern) + 1):
        transition_table.append({})
        if i == 0:
            for x in alphabet_symbols:
                transition_table[i][x] = 0
            transition_table[i][pattern[i]] = 1
        else:
            for x in alphabet_symbols:
                transition_table[i][x] = transition_table[lps][x]
            if i < len(pattern):
                transition_table[i][pattern[i]] = i + 1
                lps = transition_table[lps][pattern[i]]
    return transition_table

def fa_string_matching(text, pattern):
    delta = transition_function(pattern)
    state = 0
    shifts = []
    for s in range(len(text)):
        try:
            state = delta[state][text[s]]
        except:
            state = 0
        if state == len(pattern):
            # print(f"Przesunięcie {s + 1 - state} jest poprawne")
            shifts.append(s + 1 - state)

    return shifts

# fa_string_matching("AABAACAADAABAAABAA", "AABA")
