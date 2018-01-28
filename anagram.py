def are_anagrams(a, b):
    return ''.join(sorted(a)).lower().strip() == ''.join(sorted(b)).lower().strip()