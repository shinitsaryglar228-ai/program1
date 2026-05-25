import random

def rock_paper_scissors():
    choices = ['камень', 'ножницы', 'бумага']
    print("Добро пожаловать в 'Камень‑ножницы‑бумага'!")

    while True:
        user_choice = input("Выберите: камень, ножницы, бумага (или 'выход' для завершения): ").lower()
        if user_choice == 'выход':
            print("Спасибо за игру!")
            break

        if user_choice not in choices:
            print("Неверный ввод! Попробуйте снова.")
            continue

        computer_choice = random.choice(choices)
        print(f"Компьютер выбрал: {computer_choice}")

        # Определение победителя
        if user_choice == computer_choice:
            print("Ничья!")
        elif (user_choice == 'камень' and computer_choice == 'ножницы') or \
             (user_choice == 'ножницы' and computer_choice == 'бумага') or \
             (user_choice == 'бумага' and computer_choice == 'камень'):
            print("Вы победили!")
        else:
            print("Компьютер победил!")

# Запуск игры
rock_paper_scissors()
