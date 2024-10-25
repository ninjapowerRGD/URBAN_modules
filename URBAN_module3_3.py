def print_params(a=1, b="string", c=True):
    print(a, b, c)

#ЗАДАЧА РАСПАКОВКА:
print_params()  # вызов функции без аргументов-работает
print_params(3)  # вызов с одним аргументом-работает
print_params(b=25)  # вызов с заменой параметра b(работает, но подчеркивает)
print_params(c=[1, 2, 3])  # вызов с  заменой параметра с (работает, но подчеркивает)
print_params(7, "string2", 4)  # вызов с заменой всех параметров(работает, но подчеркивает)

#ЗАДАЧА РАСПАКОВКА ПАРАМЕТРОВ:
values_list = [111, "string3", False]
values_dict = {'a': 222, 'b': 'text-string', 'c': [1, 2, 3]}

print_params(*values_list)
print_params(**values_dict)

#ЗАДАЧА РАСПАКОВКА+ОТДЕЛЬНЫЕ ПАРАМЕТРЫ:
values_list_2 = [3.14, "STRING4"]
print_params(*values_list_2, 42)