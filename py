a = str(input("Вы хотите пройти тест на СИГМО???  "))
if a == "да" or a == "Да":
    print("ПОГНАЛЕ БРАТИШКА")
    print("ВОПРОС 1, КАК ЗОВУТ ГЛАВНОГО СИГМУ?\n1)Тайлер Дерден\n2)Влад А4\n3)Хохол")
    ans = int(input("Введи номер ответа: "))
    if ans == 1:
        print("Хорош братанчек, го некст")
        print("ВОПРОС 2, У КОГО САМЫЕ ЛУЧШЫЙ КРУЖОЧКЕ,??\n1)Мистёр Четвёрка\n2)Мистер Пятерка\n3)Мистер бизнас  ")
        ans2 = int(input("Введи номер ответа:  "))
        if ans2 == 2 or ans2 == 3:
            print("БРАТАН ТЫ ПОДТВЕРЖДЁНЫЫЙ МИСТЕР СИГМА!!!")

        else:
            print("Пока братанчик, ты ноу сигма")
    else:
        print("Ответ неверный, тест закончился бб")
else:
    a = str(input("Вы хотите отказаться от теста?  "))
    if a == "нет" or a=="Нет":

        print("ХОРОШ ЧТО ПЕРЕДУМАЛ БРО")
        print("ВОПРОС 1, КАК ЗОВУТ ГЛАВНОГО СИГМУ?\n1)Тайлер Дерден\n2)Влад А4\n3)Хохол")
        ans = str(input("Введи номер ответа: "))
        if ans == 1:
            print("Хорош братанчек, го некст")
            print("ВОПРОС 2, У КОГО САМЫЕ ЛУЧШЫЙ КРУЖОЧКЕ,??\n1)Мистёр Четвёрка\n2)Мистер Пятерка\n3)Мистер бизнас  ")
            ans2 = str(input("Введи ответ  "))
            if ans2 == 2 or ans2 == 3:
                print("БРАТАН ТЫ ПОДТВЕРЖДЁНЫЫЙ МИСТЕР СИГМА, А ХОТЕЛ ОТКАЗАТЬСЯ!!!")

            else:
                print("Пока братанчик, ты ноу сигма")
        else:
            print("Ответ неверный, тест закончился бб")
    elif a == "да" or





    import random
def get_computer_choice():
    choices = ['Камень', 'Ножницы', 'Бумага']
    return random.choice(choices)
def get_user_choice():
    choice = input("Выберите: Камень, Ножницы или Бумага? ").capitalize()
    while choice not in ['Камень', 'Ножницы', 'Бумага']:
        print("Неправильный ввод. Попробуйте еще раз.")
        choice = input("Выберите: Камень, Ножницы или Бумага? ").capitalize()
    return choice
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Ничья!"
    elif (user_choice == 'Камень' and computer_choice == 'Ножницы') or \
            (user_choice == 'Ножницы' and computer_choice == 'Бумага') or \
            (user_choice == 'Бумага' and computer_choice == 'Камень'):
        return "Вы победили!"
    else:
        return "Компьютер победил!"


def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"Вы выбрали: {user_choice}")
    print(f"Компьютер выбрал: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)
play_game()






a = float(input("Введите число кратное 3 и 5"))
if a %3 == 0 and a%5 == 0:
    print("Это число кратно на 3 и 5")
else:
    print("Это число не кратное 3 и 5")



a = int(input("Введите 1 сторону"))
b = int(input("Введите 2 сторону"))
c = int(input("Введите 3 сторону"))
if a == b == c:
    print("Ваш треугольник равносторонний")
elif a == b != c or c == a != b or c == b != a:
    print("Ваш треугольник равнобедренный")
elif a != b != c:
    print("Ваш треугольник произвольный")


import os

def read_students(filename):
    students = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split()
            name = parts[0]
            age = int(parts[1])
            grades = list(map(int, parts[2:]))
            students.append({'name': name, 'age': age, 'grades': grades})
    return students


def calculate_average(grades):
    return sum(grades) / len(grades)


def calculate_average_age(students):
    total_age = sum(student['age'] for student in students)
    return total_age / len(students)


def find_best_student(students):
    best_student = max(students, key=lambda student: calculate_average(student['grades']))
    return best_student


def sort_students_by_average_grade(students):
    students_sorted = sorted(students, key=lambda student: calculate_average(student['grades']), reverse=True)
    return students_sorted


def main():

    filename = 'students.txt'

    if not os.path.exists(filename):
        print(f'Файл {filename} не найден.')
        return

    students = read_students(filename)

    print("\nСтуденты, отсортированные по среднему баллу:")
    sorted_students = sort_students_by_average_grade(students)
    for student in sorted_students:
        average_grade = calculate_average(student['grades'])
        print(f"{student['name']}: Средний балл = {average_grade:.2f}")

    best_student = find_best_student(students)
    best_student_average = calculate_average(best_student['grades'])
    print(f"\nСтудент с наивысшим средним баллом: {best_student['name']} со средним баллом {best_student_average:.2f}")

    average_age = calculate_average_age(students)
    print(f"\nСредний возраст студентов: {average_age:.2f} лет")

if __name__ == "__main__":
    main()


def is_sigma(n):
    def check_divisor(n, divisor):
        if divisor == 1:
            return True
        if n % divisor == 0:
            return False
        return check_divisor(n, divisor - 1)
    if n <= 1:
        return False
    return check_divisor(n, n // 2)

number = int(input("Введите число: "))
result = is_sigma(number)

if result == True:
    print(f"Число {number} является сигмой")
else:
    print("Ваше число не является сигмой")