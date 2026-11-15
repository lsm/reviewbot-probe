def add(a, b):
    return a + b


def total(items):
    return sum(item["price"] * item.get("qty", 1) for item in items)


def apply_coupon(subtotal, coupon):
    if coupon["kind"] == "pct":
        return subtotal * (1 - coupon["pct"] / 100)
    return subtotal - coupon["amount"]


def average_price(items):
    return total(items) / len(items)
