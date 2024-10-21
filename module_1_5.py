grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Джонни', 'Бильбо', 'Стив', 'Хендрик', 'Аарон'}
new = []
students_1 = list(sorted(students))
new.append(sum(grades[0]) / len(grades[0]))
new.append(sum(grades[1]) / len(grades[1]))
new.append(sum(grades[2]) / len(grades[2]))
new.append(sum(grades[3]) / len(grades[3]))
new.append(sum(grades[4]) / len(grades[4]))
new_1 = dict(zip(students_1, new))
print(new_1)
print(new_1['Бильбо'])