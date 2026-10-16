import validators

def run_validators():
    res = validators.email("test@gmail.com")
    print(f"Чи валідний email? {res}")