# if 関連

# x = -3

# if x > 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == -3:
#     print('Single')
# else:
#     print('More')


# for 学習

# fruits = ["apple", "banana", "cherry"]

# for i, fruit in enumerate(fruits):
#     print(i, fruit)


# for i in range(1, 5):
#     print(i)


# fruits = ["apple", "banana", "orange"]

# for fruit in fruits:
#     print(fruit)


# 0〜9 の中から 偶数だけ表示せよ。

# for i in range(10):
#     if i % 2 == 0:
#         print(i)


## 問題4：合計を求める

# 1〜10 の合計を計算して表示せよ。

# total = 0

# for i in range(1, 11):
#     total += i
#     print(total)


## 問題5：番号付きで表示

# 次のリストを

# `0 apple`
# `1 banana`
# `2 orange`

# の形で表示せよ。


# fruits = ["apple", "banana", "orange"]

# for i, fruit in enumerate(fruits):
#     print(i, fruit)



# dictは 「名前（キー）→ 値」 の対応表。

person = {
    "name": "Taro",
    "age": 20,
    "job": "Engineer"
}

# print(person["name"], person["age"])

# "name" → キー key
# "Taro" → 値  person[key]

# for key in person:
#     print(key, person[key])

# for key, value in person.items():
#     print(key, value)



# ログ一覧を１行ずつ処理する

# logs = [" server started ", " user logged in ", " error occurred "]

# for log in logs:
#     print(f"LOG: {log}")






