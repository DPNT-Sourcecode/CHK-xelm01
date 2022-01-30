from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    for item in skus:
        if item not in "ABCD":
            return -1

