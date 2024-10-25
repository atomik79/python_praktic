
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
new_list = []
index_number = 0
while index_number < len(my_list):
    if my_list[index_number] > 0 and my_list[index_number] != 0:
        new_list.append(my_list[index_number])
    elif my_list[index_number] < 0:
        break
    index_number = index_number + 1
print(new_list)

first_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
second_list = []
digit = 0
while digit < len(first_list):
    if first_list[digit] < 0:
        break
    elif first_list[digit] != 0:
        second_list.append(first_list[digit])
    digit = digit + 1
print(*second_list, sep=" " "\n")