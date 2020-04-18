def prefix_function(pattern):
    prefix_array = [0 for _ in range(len(pattern))]

    pat_pos = 0
    for i in range(1, len(pattern)):
        while pat_pos > 0 and pattern[pat_pos] != pattern[i]:
            pat_pos = prefix_array[pat_pos - 1]

        if pattern[pat_pos] == pattern[i]:
            pat_pos += 1

        prefix_array[i] = pat_pos

    return prefix_array


def kmp(s, pattern):
    prefix_array = prefix_function(pattern)
    result = []
    pat_pos = 0
    m = len(pattern)

    for idx, a in enumerate(s):
        while pat_pos > 0 and pattern[pat_pos] != a:
            pat_pos = prefix_array[pat_pos - 1]

        if pattern[pat_pos] == a:
            pat_pos += 1

            if pat_pos == m:
                result.append(idx + 1 - m)
                pat_pos = prefix_array[pat_pos - 1]

    return result

#print(kmp_search("AABAACAADAABAAABAA", "AABA"))