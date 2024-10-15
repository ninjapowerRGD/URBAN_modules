calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    string_info_tuple = (len(string), string.upper(), string.lower())
    return string_info_tuple


def is_contains(string, list_to_search):
    count_calls()
    return user_string in user_list


user_string = input("Введите любую строку:").casefold()
user_list = input("Введите список:").casefold()

info_result = string_info(user_string)
print("Информация о строке:", info_result)

contains_result = is_contains(user_string, user_list)
print("Наличие строки в списке:", contains_result)

print("Количество функций:", calls)
