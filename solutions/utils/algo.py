from collections import Counter
from functools import reduce


def common_chars(strings):
    if not strings:
        return []

    counter = [Counter(s) for s in strings]
    common_counter = reduce(lambda x, y: x & y, counter)

    results = []
    for char, count in common_counter.items():
        results.extend([char] * count)

    return results
