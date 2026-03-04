""" ICHW6"""

def union(s1, s2):
    result = set()
    for x in s1:
        result.add(x)
    for x in s2:
        result.add(x)
    return result

def difference(s1, s2):
    result = set()
    for x in s1:
        if x not in s2:
            result.add(x)
    return result

def is_subset(s1, s2):
    for x in s1:
        if x not in s2:
            return False
    return True

def are_disjoint(s1, s2):
    for x in s1:
        if x in s2:
            return False
    return True

def symmetric_difference(s1, s2):
    result = set()
    for x in s1:
        if x not in s2:
            result.add(x)
    for x in s2:
        if x not in s1:
            result.add(x)
    return result

def cartesian_product(s1, s2):
    result = set()
    for x in s1:
        for y in s2:
            result.add((x, y))
    return result

def union_2(*s1):
    result = set()
    for s in s1:
        for x in s:
            result.add(x)
    return result

def isdisjoint_2(*s1):
    seen = set()
    for s in s1:
        for x in s:
            if x in seen:
                return False
            seen.add(x)
    return True

def is_well_formed(s):
    stack = []
    matching = {')': '(', '}': '{', ']': '['}
    for ch in s:
        if ch in '({[':
            stack.append(ch)
        elif ch in ')}]':
            if not stack or stack[-1] != matching[ch]:
                return False
            stack.pop()
    return len(stack) == 0

def rpn(s):
    stack = []
    for ch in s:
        if ch.isdigit():
            stack.append(int(ch))
        else:
            b = stack.pop()
            a = stack.pop()
            if ch == '+':
                stack.append(a + b)
            elif ch == '-':
                stack.append(a - b)
            elif ch == '*':
                stack.append(a * b)
    return stack[0]

def account_audit(trial, paid, banned):
    t = set(trial)
    p = set(paid)
    b = set(banned)
    return {
        "active":             (t | p) - b,
        "upgrade_candidates": t - p - b,
        "conflicts":          b & (t | p),
        "all_known":          t | p | b,
    }
