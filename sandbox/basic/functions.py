

# def add(a, b):
#     # ２つの数値を足して返す
#     result = a + b
#     return result 


# def greet(name):
#     # 名前を受け取って挨拶を返す
#     return f"Hello, {name}!"

# def main():
#     #引数を渡して関数を呼ぶ
#     total = add(3, 5)
#     print(f"add result: {total}")

#     message = greet("Hiroaki")
#     print(message)

# if __name__ == "__main__":
#     main()

# このスクリプトは、基本的な関数の定義と使用例を示しています。



def is_even(number):
    return number % 2 == 0


def main():
    for i in range(5):
        print(i, is_even(i))

if __name__ == "__main__":
    main()

