# Q: List of clothes prices and we have to get the list
# of discounted price

# ip:

# price= [100,50,..]
# discount=10

# op:

# new_price= [90,45,..]


def apply_discount(price, discount_rate):
    return price - (price * discount_rate / 100)  # Discount rate expression


product_price = [100, 50, 453, 120, 200]

# for-loop

ans_list = []
for price in product_price:
    discounted_price = apply_discount(price, 10)
    ans_list.append(discounted_price)


print("using loop ans_list : ", ans_list)


# 2nd way using map

# map returns a map value (not a list)
ans_map = map(lambda a: apply_discount(a, 10), product_price)

print("using map :", list(ans_map))


                      # [100, 50, 453, 120, 200]
using loop ans_list :  [90.0, 45.0, 407.7, 108.0, 180.0]
using map :            [90.0, 45.0, 407.7, 108.0, 180.0]