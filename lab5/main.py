# main.py - головний файл гри. Запуск: python main.py
from inventory import Inventory
from data import INGREDIENTS, POTIONS
from utils import ask_int, ask_text
import actions

START_GOLD = 100
GOAL_GOLD = 1000   # щоб виграти
MAX_DAYS = 30      # за скільки днів


def check_end(day, gold, ingredient_inv, potion_inv):
    """Повертає 'win', 'lose' або None (гра триває)."""
    try:
        if gold >= GOAL_GOLD:
            return "win"
        if day > MAX_DAYS:
            return "lose"
        cheapest = min(INGREDIENTS.values())
        if gold < cheapest and ingredient_inv.is_empty() and potion_inv.is_empty():
            return "lose"  # зовсім нічого немає
    except Exception as e:
        print("Помилка перевірки кінця гри:", e)
    return None


def play():
    ingredient_inv = Inventory("Інгредієнти", 25, 25)
    potion_inv = Inventory("Зілля", 10, 10)
    gold = START_GOLD
    day = 1

    print("=== АЛХІМІК ===")
    print(f"Мета: назбирати {GOAL_GOLD} золота за {MAX_DAYS} днів.")
    print(f"Інгредієнтів у грі: {len(INGREDIENTS)}, видів зілля: {len(POTIONS)}")

    while True:
        print(f"\n===== День {day}/{MAX_DAYS} | Золото: {gold} =====")
        actions.give_daily_ingredients(ingredient_inv)

        while True:  # дії протягом дня
            print("\n1-Інвентар 2-Рецепти 3-Зварити зілля 4-Купити інгредієнт 5-Закінчити день")
            choice = ask_int("Ваш вибір: ", 1, 5)
            if choice == 1:
                ingredient_inv.show()
                potion_inv.show()
            elif choice == 2:
                actions.show_recipes()
            elif choice == 3:
                actions.craft_potion(ingredient_inv, potion_inv)
            elif choice == 4:
                gold = actions.buy_ingredient(gold, ingredient_inv)
            else:
                break

        # кінець дня - продаж зілль
        answer = ask_text("Продати всі зілля? (так/ні): ")
        if answer in ("так", "т", "y", "yes"):
            gold = actions.sell_potions(gold, potion_inv)

        day += 1
        result = check_end(day, gold, ingredient_inv, potion_inv)
        if result == "win":
            print(f"\nВІТАЮ! У вас {gold} золота. Ви стали Головним Алхіміком королівства!")
            break
        if result == "lose":
            print(f"\nПРОГРАШ. У вас лише {gold} золота. Ваша лабораторія закрилась...")
            break


def main():
    try:
        play()
    except SystemExit:
        pass
    except Exception as e:
        print("Критична помилка гри:", e)


if __name__ == "__main__":
    main()
