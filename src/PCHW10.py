def first_repeated_char(s):
    seen = set()
    for char in s:
        if char in seen:
            return char
        seen.add(char)
    return ""


def same_letters(s1, s2):
    counts = {}
    for char in s1:
        counts[char] = counts.get(char, 0) + 1
    for char in s2:
        counts[char] = counts.get(char, 0) - 1
    return all(v == 0 for v in counts.values())
