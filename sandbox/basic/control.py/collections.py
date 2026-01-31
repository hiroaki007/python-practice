"""
    目的：
    -　list / dict の基本
    -　件数（count）と合計(sum)
    - for + dict による集計
"""


# 1. list の基本　

numbers = [100, 200, 300, 100, 200]

print('numbers:', numbers)
print("first:", numbers[1])
print("length:", len(numbers))


# 2. dict の基本

prices = {
    "apple": 100,
    "banana": 200,
    "oringe": 150,
}

print("\nprices:", prices)
print("apple price:", prices["apple"])


# 3. count（件数集計）

items = ["apple", "banana", "apple", "orange", "apple"]

count_by_item = {}

for item in items:
    if item not in count_by_item:
        count_by_item[item] = 0
    count_by_item[item] += 1

print("\ncount_by_item:", count_by_item)


# 4. sum(合計金額)

amounts = [100, 200, 300]

total = 0
for amount in amounts:
    total += amount

print("\ntotal amount:", total)


# 5. for + dict(実務で使う形)
#　 商品ごとに売上合計を作る

sales = [
    ("apple", 100),
    ("banana", 200),
    ("apple", 150),
    ("orange", 300),
    ("banana", 100),
]

summary = {}

for product, price in sales:
    if product not in summary:
        summary[product] = 0
    summary[product] += price


print("\nsales summary:")
for product, total_price in summary.items():
    print(f"{product}: {total_price}")






