from collections import Counter

PRICE_TABLE = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
    "F": 10,
    "G": 20,
    "H": 10,
    "I": 35,
    "J": 60,
    "K": 80,
    "L": 90,
    "M": 15,
    "N": 40,
    "O": 10,
    "P": 50,
    "Q": 30,
    "R": 50,
    "S": 30,
    "T": 20,
    "U": 40,
    "V": 50,
    "W": 20,
    "X": 90,
    "Y": 10,
    "Z": 50,
}
SPECIAL_OFFERS = {
    "A": [(5, 200), (3, 130)],
    "B": [(2, 45)],
    "F": [(3, 20)],
    "H": [(10, 80), (5, 45)],
    "K": [(2, 150)],
    "P": [(5, 200)],
    "Q": [(3, 80)],
    "U": [(4, 120)],
    "V": [(3, 130), (2, 90)],
}
SPECIAL_OFFERS_MULTI_ITEMS = {
    "E": (2, "B"),
    "N": (3, "M"),
    "R": (3, "Q"),
}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # Return -1 if the item is not in the table
    for item in skus:
        if item not in PRICE_TABLE:
            return -1

    total = 0
    skus_counter = Counter(skus)

    # Apply special offers for multiple items first
    for item, (count, free_item) in SPECIAL_OFFERS_MULTI_ITEMS.items():
        skus_counter[free_item] -= skus_counter[item] // count
        if skus_counter[free_item] < 0:
            skus_counter[free_item] = 0

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




