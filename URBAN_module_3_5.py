while True:
    number = input("Напиши любое число: ") #its string

    # Удаляем запятые и точки из строки
    number = number.replace(",", "").replace(".", "")

    # Проверяем,что строка только из цифр
    if not number.isdigit():
        print("Введенное значение не является числом. Пожалуйста, попробуйте еще раз.")
        continue

    # если длина строки равна 1, возвращаем это число как целое
    def get_multiplied_digits(number):
        if len(number) == 1:
            return int(number) # результат переводив в int

        # тут умножаем первую цифру на результат вызова функции с оставшимися цифрами
        first = int(number[0])
        return first * get_multiplied_digits(number[1:]) #рекурсия


    result = get_multiplied_digits(number)
    print(result)
    break