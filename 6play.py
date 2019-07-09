from collections import Counter
def is_isomorphic(y,s):
    y_counts = list(Counter(y).values())
    y_counts.sort()
    s_counts = list(Counter(s).values())
    s_counts.sort()
    if y_counts == s_counts:
        return 'yes'
    return 'no'
y,s=input().split()
print(is_isomorphic(y,s))
