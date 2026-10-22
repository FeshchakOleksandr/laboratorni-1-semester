# data.py - тут створюються інгредієнти (200) і зілля (50)
import random

BASES = ["Корінь", "Листок", "Гриб", "Квітка", "Ягода",
         "Насіння", "Мох", "Кора", "Пилок", "Сік"]
OWNERS = ["дракона", "фенікса", "вовка", "ворона", "місяця",
          "сонця", "туману", "грому", "льоду", "вогню",
          "болота", "печери", "гори", "моря", "тіні",
          "зорі", "вітру", "кришталю", "привида", "лісу"]

EFFECTS = ["лікування", "сили", "швидкості", "невидимості", "мудрості",
           "стійкості", "удачі", "зору", "дихання", "енергії"]
TIERS = ["слабке", "звичайне", "велике", "майстерне", "легендарне"]


def create_ingredients():
    """Повертає словник {назва: ціна}. 10 * 20 = 200 різних інгредієнтів."""
    rnd = random.Random(5)  # однакові ціни при кожному запуску
    result = {}
    try:
        for base in BASES:
            for owner in OWNERS:
                result[f"{base} {owner}"] = rnd.randint(5, 15)
    except Exception as e:
        print("Помилка створення інгредієнтів:", e)
    return result


def create_potions(ingredients):
    """Повертає словник {назва: {"recipe": [..], "price": число}}. 10 * 5 = 50 зілль."""
    rnd = random.Random(7)
    names = list(ingredients.keys())
    result = {}
    try:
        for effect in EFFECTS:
            for level, tier in enumerate(TIERS):
                recipe = rnd.sample(names, 2)  # 2 різні інгредієнти
                cost = sum(ingredients[i] for i in recipe)
                price = cost * 2 + level * 10
                result[f"Зілля {effect} ({tier})"] = {"recipe": recipe, "price": price}
    except Exception as e:
        print("Помилка створення зілль:", e)
    return result


INGREDIENTS = create_ingredients()
POTIONS = create_potions(INGREDIENTS)
