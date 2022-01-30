from collections import Counter

PRICE_TABLE = {"A": 50, "B": 30, "C": 20, "D": 15}
SPECIAL_OFFERS = {"A": (3, 130), "B": (2, 45)}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    for item in skus:
        if item not in PRICE_TABLE:
            return -1

    total = 0

    skus_counter = Counter(skus)
    for item, count in skus_counter.items():
        if item in SPECIAL_OFFERS:
            total += (
                count // SPECIAL_OFFERS[item][0] * SPECIAL_OFFERS[item][1]
                + count % SPECIAL_OFFERS[item][0] * PRICE_TABLE[item]
            )
        else:
            total += count * PRICE_TABLE[item]

    return total
