from collections import Counter

PRICE_TABLE = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40, "F": 10}
SPECIAL_OFFERS = {"A": [(5, 200), (3, 130)], "B": [(2, 45)], "F": [(3, 20)]}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # Return -1 if the item is not in the table
    for item in skus:
        if item not in PRICE_TABLE:
            return -1

    total = 0
    skus_counter = Counter(skus)

    # Special offer for E
    skus_counter["B"] -= skus_counter["E"] // 2
    if skus_counter["B"] < 0:
        skus_counter["B"] = 0

    # Compute total using special offers and individual prices
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




