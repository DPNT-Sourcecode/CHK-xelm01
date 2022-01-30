from collections import Counter

PRICE_TABLE = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40}
SPECIAL_OFFERS = {"A": [(5, 200), (3, 130)], "B": [(2, 45)]}

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
            remainder_count = count
            for special_offer in SPECIAL_OFFERS[item]:
                total += remainder_count // special_offer[0] * special_offer[1]
                remainder_count %= special_offer[0]
            total += remainder_count * PRICE_TABLE[item]
        else:
            total += count * PRICE_TABLE[item]

    return total


