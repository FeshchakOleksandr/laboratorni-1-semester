# inventory.py - клас інвентаря зі слотами та стаками


class Inventory:
    def __init__(self, title, max_slots, stack_size):
        self.title = title
        self.max_slots = max_slots
        self.stack_size = stack_size
        self.slots = []  # кожен слот: [назва, кількість]

    def add(self, item, amount=1):
        """Додає предмети. Повертає, скільки реально влізло."""
        added = 0
        try:
            while amount > 0:
                placed = False
                for slot in self.slots:
                    if slot[0] == item and slot[1] < self.stack_size:
                        take = min(self.stack_size - slot[1], amount)
                        slot[1] += take
                        amount -= take
                        added += take
                        placed = True
                        break
                if not placed:
                    if len(self.slots) < self.max_slots:
                        self.slots.append([item, 0])  # новий порожній слот
                    else:
                        break  # місця немає
        except TypeError:
            print("Помилка: кількість має бути числом")
        return added

    def count(self, item):
        total = 0
        try:
            for slot in self.slots:
                if slot[0] == item:
                    total += slot[1]
        except Exception as e:
            print("Помилка підрахунку:", e)
        return total

    def remove(self, item, amount=1):
        """Видаляє предмети. Повертає True, якщо вдалося."""
        try:
            if self.count(item) < amount:
                return False
            for slot in self.slots[::-1]:
                if slot[0] == item and amount > 0:
                    take = min(slot[1], amount)
                    slot[1] -= take
                    amount -= take
            self.slots = [s for s in self.slots if s[1] > 0]  # прибираємо порожні
            return True
        except Exception as e:
            print("Помилка видалення:", e)
            return False

    def is_empty(self):
        return len(self.slots) == 0

    def show(self):
        print(f"--- {self.title} (слотів {len(self.slots)}/{self.max_slots}) ---")
        try:
            if not self.slots:
                print("  порожньо")
            for i, slot in enumerate(self.slots, 1):
                print(f"  {i}. {slot[0]} x{slot[1]}")
        except Exception as e:
            print("Помилка показу:", e)
