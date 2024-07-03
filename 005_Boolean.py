# Системы счисления. Двоичная система:

# 00000000 - это байт (8 бит), его значение ноль
# 00000001 - это единица
# 00000010 - это двойка
# 00000011 - это тройка
# 00000100 - это четверка
# 00000101 - это пятерка
# 00000110 - это шестерка
# 00000111 - это семерка
# 11111111 - это 255



# Системы счисления. Шеснадцатиричная система:

# Помимо обычных цифр, в нее добавлены 6 цифр:
# A - 10
# B - 11
# C - 12
# D - 13
# E - 14
# F - 15
#

# 8 + 5 = 13 - это в 10-й системе
# 8 + 5 = D - это в 16-й системе
# 9 + C = 15 (21)
# В 16-й системе байт это FF
#
#


def main():
    x = True                    # х - переменная логического типа
    y = False
    print(type(x), type(y))
    print(x and y)              # and - логическое умножение, конъюнкция
    y = True
    print(x and y)
    print(x or y)               # or - логическое сложение, дизъюнкция
    x = False
    y = False
    print(x or y)

def ages():
    igors_age = 31.2
    davids_age = 52
    johns_age = 10
    if igors_age > davids_age and igors_age > johns_age:
        print("Игорь старше всех")
    elif davids_age > igors_age and davids_age > johns_age:
        print("Давид старше всех")
    else:
        print("Джон старше всех")


    john_is_youngest = johns_age < igors_age and johns_age < davids_age
    print(type(john_is_youngest))
    if john_is_youngest:
        print("Джон самый младший")

    if igors_age == davids_age and igors_age == johns_age:
        print("Все одинакового возвраста")
    if igors_age != davids_age:
        print("Игорь и Давид разного возвраста")
    if igors_age <= davids_age and igors_age >= johns_age:
        print("Игорь не старше Давида и не моложе Джона")




if __name__ == "__main__":
    main()
    ages()
