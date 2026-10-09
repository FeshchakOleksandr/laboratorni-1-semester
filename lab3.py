"""Лабораторна робота 3: міні магазин в консолі."""

ADMIN_PASSWORD: str = "admin123"

# Каталог: назва -> ціна та залишок на складі
products: dict = {
    "Хліб": {"price": 25.5, "stock": 10},
    "Молоко": {"price": 42.0, "stock": 8},
    "Сир": {"price": 180.75, "stock": 5},
    "Яблука": {"price": 35.2, "stock": 20},
}

# Кошик: назва -> кількість
cart: dict = {}


def format_price(price: float) -> str:
    """Повертає ціну у форматі ххх.ххгрн."""
    return f"{price:06.2f}грн"


def line_total(name: str) -> float:
    """Повертає суму за товар у кошику (ціна * кількість)."""
    return products[name]["price"] * cart[name]


def total_price() -> float:
    """Повертає загальну суму кошика."""
    total = 0.0
    for name in cart:
        total += line_total(name)
    return total


def read_int(text: str) -> int:
    """Читає ціле число, при помилці повертає 0."""
    value = input(text)
    return int(value) if value.isdigit() else 0


def show_catalog() -> None:
    """Показує каталог товарів."""
    print("\n--- Каталог ---")
    for name, info in products.items():
        print(f"{name}: {format_price(info['price'])}")


def add_to_cart() -> None:
    """Додає товар в кошик."""
    name = input("Назва товару: ")
    if name not in products:
        print("Такого товару немає")
        return
    count = read_int("Кількість: ")
    in_cart = cart.get(name, 0)
    if count <= 0 or in_cart + count > products[name]["stock"]:
        print("Некоректна кількість або немає на складі")
        return
    cart[name] = in_cart + count
    print("Додано в кошик")


def remove_from_cart() -> None:
    """Видаляє товар з кошика."""
    name = input("Назва товару для видалення: ")
    if name in cart:
        del cart[name]
        print("Видалено")
    else:
        print("Цього товару немає в кошику")


def show_cart() -> None:
    """Показує кошик і загальну суму."""
    print("\n--- Кошик ---")
    for name in cart:
        print(f"{name} x{cart[name]} = {format_price(line_total(name))}")
    print(f"Разом: {format_price(total_price())}")


def buy() -> None:
    """Купує товари з кошика і зменшує залишки."""
    if not cart:
        print("Кошик порожній")
        return
    show_cart()
    for name in cart:
        products[name]["stock"] -= cart[name]
    cart.clear()
    print("Дякуємо за покупку!")


def admin_panel() -> None:
    """Вхід адміністратора та перегляд залишків."""
    if input("Пароль: ") != ADMIN_PASSWORD:
        print("Невірний пароль")
        return
    print("\n--- Залишки на складі ---")
    for name, info in products.items():
        print(f"{name}: {info['stock']} шт.")


def main() -> None:
    """Головне меню програми."""
    actions = {
        "1": show_catalog,
        "2": add_to_cart,
        "3": remove_from_cart,
        "4": show_cart,
        "5": buy,
        "6": admin_panel,
    }
    while True:
        print(
            "\n1 - Каталог\n2 - Додати в кошик\n3 - Видалити з кошика\n"
            "4 - Кошик\n5 - Купити\n6 - Адміністратор\n0 - Вихід"
        )
        choice = input("Ваш вибір: ")
        if choice == "0":
            break
        if choice in actions:
            actions[choice]()
        else:
            print("Невірний пункт")


if __name__ == "__main__":
    main()