# Лямбда: ціна у форматі 100.00грн
format_price = lambda price: f"{price:.2f}грн"

# Товари магазину: кожен товар - це словник
products = [
    {"id": 1, "name": "Хліб", "price": 25.5, "stock": 20},
    {"id": 2, "name": "Молоко", "price": 42, "stock": 15},
    {"id": 3, "name": "Навушники", "price": 750, "stock": 5},
    {"id": 4, "name": "Мишка", "price": 320.99, "stock": 8},
]

cart = {}  # кошик: id товару -> кількість


def find_product(id):
    # Лямбда: шукаємо товар за id
    result = list(filter(lambda p: p["id"] == id, products))
    if result:
        return result[0]
    return None


def show_catalog():
    for p in products:
        print(p["id"], p["name"], format_price(p["price"]))


def add_to_cart():
    p = find_product(int(input("ID товару: ")))
    if p is None:
        print("Такого товару немає")
        return
    qty = int(input("Кількість: "))
    if cart.get(p["id"], 0) + qty > p["stock"]:
        print("Немає стільки на складі")
        return
    cart[p["id"]] = cart.get(p["id"], 0) + qty
    print("Додано в кошик")


def remove_from_cart():
    id = int(input("ID товару: "))
    if id in cart:
        del cart[id]
        print("Видалено")
    else:
        print("Цього товару немає в кошику")


def cart_sum():
    # Лямбда: сума кошика
    return sum(map(lambda item: find_product(item[0])["price"] * item[1], cart.items()))


def show_cart():
    if not cart:
        print("Кошик порожній")
        return
    for id, qty in cart.items():
        p = find_product(id)
        print(p["name"], "x", qty, "=", format_price(p["price"] * qty))
    print("Разом:", format_price(cart_sum()))


def buy():
    if not cart:
        print("Кошик порожній")
        return
    total = cart_sum()
    for id, qty in cart.items():
        find_product(id)["stock"] -= qty
    cart.clear()
    print("Куплено! Сплачено:", format_price(total))


def admin():
    if input("Пароль: ") == "admin123":
        for p in products:
            print(p["name"], "- залишок:", p["stock"])
    else:
        print("Невірний пароль")


def main():
    # Головне меню
    while True:
        print("\n1 - Каталог")
        print("2 - Додати в кошик")
        print("3 - Видалити з кошика")
        print("4 - Показати кошик")
        print("5 - Купити")
        print("6 - Адміністратор")
        print("0 - Вихід")
        choice = input("Вибір: ")

        if choice == "1":
            show_catalog()
        elif choice == "2":
            add_to_cart()
        elif choice == "3":
            remove_from_cart()
        elif choice == "4":
            show_cart()
        elif choice == "5":
            buy()
        elif choice == "6":
            admin()
        elif choice == "0":
            break


if __name__ == "__main__":
    main()
