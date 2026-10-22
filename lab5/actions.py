# actions.py - дії гравця: рецепти, варіння, купівля, продаж, видача інгредієнтів
import random
from data import INGREDIENTS, POTIONS
from utils import ask_int, ask_text

INGREDIENTS_PER_DAY = 5


def give_daily_ingredients(ingredient_inv):
    """Видає 5 випадкових інгредієнтів на початку дня."""
    try:
        names = random.sample(list(INGREDIENTS.keys()), INGREDIENTS_PER_DAY)
        print("Вам видали інгредієнти на день:")
        for name in names:
            added = ingredient_inv.add(name, 1)
            if added:
                print(f"  + {name}")
            else:
                print(f"  ! {name} - немає місця, пропало")
    except Exception as e:
        print("Помилка видачі інгредієнтів:", e)


def show_recipes():
    try:
        for name, info in POTIONS.items():
            recipe = " + ".join(info["recipe"])
            print(f"{name}: {recipe} (ціна {info['price']})")
    except Exception as e:
        print("Помилка показу рецептів:", e)


def craft_potion(ingredient_inv, potion_inv):
    """Показує, що можна зварити зараз, і варить обране."""
    try:
        available = []
        for name, info in POTIONS.items():
            if all(ingredient_inv.count(i) >= 1 for i in info["recipe"]):
                available.append(name)
        if not available:
            print("З вашими інгредієнтами нічого зварити не можна.")
            return
        print("Можна зварити:")
        for i, name in enumerate(available, 1):
            print(f"  {i}. {name} (ціна {POTIONS[name]['price']})")
        choice = ask_int("Номер зілля (0 - назад): ", 0, len(available))
        if choice == 0:
            return
        name = available[choice - 1]
        if potion_inv.add(name, 1) == 0:
            print("Інвентар зілль повний! Спочатку продайте зілля.")
            return
        for ingredient in POTIONS[name]["recipe"]:
            ingredient_inv.remove(ingredient, 1)
        print(f"Ви зварили: {name}")
    except Exception as e:
        print("Помилка варіння:", e)


def buy_ingredient(gold, ingredient_inv):
    """Купівля інгредієнта за пошуком по назві. Повертає нову кількість золота."""
    try:
        word = ask_text("Частина назви інгредієнта (напр. 'корінь дракона'): ")
        found = [n for n in INGREDIENTS if word in n.lower()][:10]
        if not found:
            print("Нічого не знайдено.")
            return gold
        for i, name in enumerate(found, 1):
            print(f"  {i}. {name} - {INGREDIENTS[name]} золота")
        choice = ask_int("Номер (0 - назад): ", 0, len(found))
        if choice == 0:
            return gold
        name = found[choice - 1]
        price = INGREDIENTS[name]
        if gold < price:
            print("Не вистачає золота!")
            return gold
        if ingredient_inv.add(name, 1) == 0:
            print("Інвентар інгредієнтів повний!")
            return gold
        print(f"Куплено: {name}")
        return gold - price
    except Exception as e:
        print("Помилка купівлі:", e)
        return gold


def sell_potions(gold, potion_inv):
    """Продає всі зілля. Повертає нову кількість золота."""
    try:
        if potion_inv.is_empty():
            print("Зілль для продажу немає.")
            return gold
        total = 0
        for name, info in POTIONS.items():
            amount = potion_inv.count(name)
            if amount > 0:
                total += amount * info["price"]
                potion_inv.remove(name, amount)
        print(f"Ви продали зілля і заробили {total} золота.")
        return gold + total
    except Exception as e:
        print("Помилка продажу:", e)
        return gold
