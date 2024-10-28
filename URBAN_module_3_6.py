data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(structure):
    total_amount = 0

    for element in structure:
        if isinstance(element, int):
            total_amount += element

        elif isinstance(element, str):
            total_amount += len(element)

        elif isinstance(element, list):
            # расчёт списка
            for item in element:
                total_amount += calculate_structure_sum([item])

        elif isinstance(element, tuple):
            # расчёт кортежа
            for item in element:
                total_amount += calculate_structure_sum([item])

        elif isinstance(element, set):
            # расчет множества
            for item in element:
                total_amount += calculate_structure_sum([item])

        elif isinstance(element, dict):
            for key, value in element.items():
                total_amount += calculate_structure_sum([key, value])

    return total_amount

result = calculate_structure_sum(data_structure)
print(result)