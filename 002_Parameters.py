# Функция main задана с параметром name. Его значение по умолчанию - World.
def main(name="World"):
    print("Hello " + name + '.')
    print('Hello {n} (Использование функции format).'.format(n=name))
    print(f'Hello {name} (Так работает f-string).')


if __name__ == "__main__":

# Функция main вызывается с различными аргументами.

    main("Vlad")
    main("Igor")
    main()
