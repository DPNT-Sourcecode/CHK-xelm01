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
    "K": 70,  # 80,
    "L": 90,
    "M": 15,
    "N": 40,
    "O": 10,
    "P": 50,
    "Q": 30,
    "R": 50,
    "S": 20,  # 30,
    "T": 20,
    "U": 40,
    "V": 50,
    "W": 20,
    "X": 17,  # 90,
    "Y": 20,  # 10,
    "Z": 21,  # 50,
}
# NOTE: Add offers in descending order of number of items
SPECIAL_OFFERS = {
    "A": [(5, 200), (3, 130)],
    "B": [(2, 45)],
    "F": [(3, 20)],
    "H": [(10, 80), (5, 45)],
    "K": [(2, 120)],  # [(2, 150)],
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
GROUP_OFFERS = {"STXYZ": (3, 45)}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # Return -1 if the item is not in the table
    for item in skus:
        if item not in PRICE_TABLE:
            return -1

    total = 0
    skus_counter = Counter(skus)

    # Apply special offers for multiple items
    for item, (count, free_item) in SPECIAL_OFFERS_MULTI_ITEMS.items():
        skus_counter[free_item] -= skus_counter[item] // count
        if skus_counter[free_item] < 0:
            skus_counter[free_item] = 0

    # Apply group offers
    for group, (group_count, group_price) in GROUP_OFFERS.items():
        group_total_count = sum(
            count for item, count in skus_counter.items() if item in group
        )
        total += (group_total_count // group_count) * group_price

        # Remove items in desceding order of their individual price
        number_of_items_to_remove = group_total_count - group_total_count % group_count
        group = sorted(group, key=lambda x: PRICE_TABLE[x], reverse=True)
        for item in group:
            old_count = skus_counter[item]
            skus_counter[item] -= number_of_items_to_remove
            if skus_counter[item] < 0:
                skus_counter[item] = 0
            number_of_items_to_remove -= old_count
            if number_of_items_to_remove <= 0:
                break

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
