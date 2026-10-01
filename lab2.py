users = {
    "ivan": ["1111", [12, 10, 8, 4, 11]],
    "olga": ["2222", [5, 6, 3, 9, 12, 7]],
    "petro": ["3333", [2, 4, 5, 8, 10]],
    "maria": ["4444", [11, 12, 12, 9, 1]],
}

login = input("Логін: ")

if login in users:
    ok = False

    for i in range(3):
        password = input("Пароль: ")
        if password == users[login][0]:
            ok = True
            break
        else:
            print("Невірний пароль. Залишилось спроб:", 2 - i)

    if ok:
        grades = users[login][1]
        print("Ваші оцінки:", grades)

        good = 0
        bad = 0
        for g in grades:
            if g >= 5:
                good += 1
            else:
                bad += 1

        print("Задовільних (5-12):", good)
        print("Незадовільних (1-4):", bad)
    else:
        print("Спроби закінчились. Доступ закрито.")
else:
    print("Такого користувача немає")