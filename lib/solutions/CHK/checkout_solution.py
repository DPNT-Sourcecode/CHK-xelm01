from collections import Counter

PRICE_TABLE = {"A": 50, "B": 30, "C": 20, "D": 15}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    for item in skus:
        if item not in "ABCD":
            return -1

    total = 0

    skus_counter = Counter(skus)
    for item, count in skus_counter.items():
        if item == "A":
            total += count // 3 * 130 + count % 3 * 50

    return total


