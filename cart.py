def add(a, b):
    return a + b


def total(items):
    return sum(item["price"] * item.get("qty", 1) for item in items)
