def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:

        try:
            result += i
        except TypeError as exc:
            incorrect_data += 1
            print(f"введите корректные данные {exc}: {type(i)}")

    return result, incorrect_data

def calculate_average(numbers):
    meaning_average = 0
    try:
        numbers_len = len(numbers)
        sum_numbers, incorrect_data = personal_sum(numbers)
        meaning_average = sum_numbers /(numbers_len - incorrect_data)
    except TypeError as exc:
        print(f"введите корректные данные: {exc}, {type(numbers)}")
        meaning_average = None
    except ZeroDivisionError as exc:
        print(f"данные отсутствуют")
    return meaning_average

print({calculate_average(["7", 4, 5])})
calc_ = calculate_average([5,"i","p",7,8,"e"])
calc_2 = calculate_average([9, 7, 4, 3,12,20])
print(round(calc_2))
print(round(calc_, 2))
