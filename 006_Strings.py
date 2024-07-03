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
    hello = "Hello World"       # hello - строковая переменная (str, string)
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


if __name__ == "__main__":
    # main()
    check_type()
