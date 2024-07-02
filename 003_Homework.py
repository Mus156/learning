def square(x):
    print(f'{x} в квадрате равен {x * x}')


# Функция greeting задана с параметром name. Его значение по умолчанию - World.
def greeting(name="World"):
    print("Hello " + name + '.')
    print('Hello {n} (Использование функции format).'.format(n=name))
    print(f'Hello {name} (Так работает f-string).')


if __name__ == "__main__":

# Функция greeting вызывается с различными аргументами.

    greeting()
    greeting('Влад')
    square(2)
