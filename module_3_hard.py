def calculate_structure_sum(data_structure):
    sum_ = 0

    if isinstance(data_structure, int):
        sum_ += data_structure
        print((sum_))
    elif isinstance(data_structure, str):
        sum_ += len(data_structure)
        print(sum_)
    elif isinstance(data_structure, list):
        for j in data_structure:
            sum_ += calculate_structure_sum(j)
            print(sum_)
    elif isinstance(data_structure, dict):
        for key, value in data_structure.items():
            sum_ += calculate_structure_sum(key)
            sum_ += calculate_structure_sum(value)
    elif isinstance(data_structure, tuple):
        for j in data_structure:
            sum_ += calculate_structure_sum(j)
    elif isinstance(data_structure, set):
        for j in data_structure:
            sum_ += calculate_structure_sum(j)


    return sum_

data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])]
result = calculate_structure_sum(data_structure)
print(result)
