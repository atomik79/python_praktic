import random


def list_digit():
    num = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    digit = random.choice(num)
    return digit


n = list_digit()
print(n)


def get_dict(n):
    dict_2 = {}
    dict_2.update({3: 12, 4: 13, 5: 1423, 6: 121524, 7: 162534, 8: 13172635, 9: 1218273645})
    dict_2.update({10: 141923283746, 11: 11029384756, 12: 12131511124210394857, 13: 112211310495867})
    dict_2.update({14: 1611325212343114105968, 15: 1214114232133124115106978})
    dict_2.update({16: 1317115262143531341251161079, 17: 11621531441351261171089})
    dict_2.update({18: 12151811724272163631545414513612711810, 19: 118217316415514613712811910})
    dict_2.update({20: 13141911923282183731746416515614713812911})
    dict_1 = dict_2.get(n)
    return dict_1


dig_1 = list(range(1, n))
dig_2 = list(range(1, n))
digits = []
result = ''

for i in dig_1:
    for j in dig_2:
        if i >= j:
            continue
        else:
            if n % (i + j) == 0:
                digits.append([i, j])
                result = result + str(i) + str(j)
print('number', *digits)
print("code", result)
print('Код совпал')
