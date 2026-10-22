# utils.py - безпечне введення від користувача


def ask_int(text, min_value, max_value):
    """Питає число, поки користувач не введе правильне."""
    while True:
        try:
            value = int(input(text))
            if value < min_value or value > max_value:
                raise ValueError
            return value
        except ValueError:
            print(f"Введіть ціле число від {min_value} до {max_value}!")
        except (EOFError, KeyboardInterrupt):
            print("\nВведення перервано, вихід з гри.")
            raise SystemExit


def ask_text(text):
    try:
        return input(text).strip().lower()
    except (EOFError, KeyboardInterrupt):
        print("\nВведення перервано, вихід з гри.")
        raise SystemExit
