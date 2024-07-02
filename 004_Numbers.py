def main():
    x = 123         # это переменная х, целое число, тип int
    y = 123.45      # это дробное число, тип float
    print(type(x))
    print(type(y))
    z = x + y
    print(type(z))
    x = float(x)    # Принудительно превращаем целое число в дробное
    print(type(x))
    z = x * y
    print(z)
    z = x - y
    print(z)
    z = y / x
    print(z)
    z = y // x      # Разделить с округлением в меньшую сторону
    print(z)        # Д/З - превратить результат в целое число
    z = y % x       # Найти остаток от деления
    print(z)
    print(5 % 2)

    x *= 10
    print(x)
    x += 10
    print(x)
    x -= 10
    print(x)
    x /= 10
    print(x)
    x //= 10
    print(x)
    x %= 10
    print(x)



if __name__ == "__main__":
    main()
