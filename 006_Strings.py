def type_of(var, name):
    if type(var) == bool:
        print(f"Переменная {name} - логическое значение")
    elif type(var) == int:
        print(f"Переменная {name} - целое число")
    elif type(var) == float:
        print(f"Переменная {name} - дробное число")
    elif type(var) == str:
        print(f"Переменная {name} - строка, текст")
    else:
        print(f"Не удалось определить тип переменной {name}")


def check_type():
    a = True
    b = 123
    c = "Hello"
    d = 123.45
    e = []
    type_of(a, "a")
    type_of(b, "b")
    type_of(c, "c")
    type_of(d, "d")
    type_of(e, "e")


def main():
    hello = "Hello World"  # hello - строковая переменная (str, string)
    print(type(hello))
    print(hello)
    print("ok")
    hello += " " + str(100 + 10)
    print(hello)
    hello = "100"
    age = int(hello)
    if type(age) == bool:
        print("Переменная age - целое число")
    else:
        print("Переменная age - не целое число")
    print(type(age))
    print(age + 10)
    print(type(hello))
    print('Роман Тургенева "Отцы и дети"')
    print("The 'New York Times'")

def str_methods():
    hello = 'Hello World'
    print(f'Длина фразы {hello} - {len(hello)}')            # метод len - посчитать количество символов строки
    print(hello.replace('Hello', 'Goodbye'))    # метод replace - замена части строки
    spaced = '   Hello   '
    print(f'Длина с пробелами - {len(spaced)}, длина без пробелов - {len(spaced.strip())}')     # метод strip - отбрасывает пробелы в начале и в конце
    print(hello.upper(), hello.lower())                     # метод upper, lower - поменять регистр букв
    print('ll' in hello)


if __name__ == "__main__":
    main()
    check_type()
    str_methods()
