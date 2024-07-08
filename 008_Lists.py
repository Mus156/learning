def main():
    car_models = ['Audi', 'BMW', "УАЗ"]         # В Python это означает список (list), который формируется с помощью []
    print(car_models[0])                        # В списках индексирование ведется от 0 (отсчет элементов)
    print(car_models[-1])
    for car in car_models:                      # Итерация, цикл (обработка поэлементно)
        print(car)
    last = len(car_models) - 1
    print(f'Последний в списке - {car_models[last]}')               # Номер последнего элента в спимке на 1 меньше длины списка
    car_models.append('ОКА')
    car_models.append('УАЗ')

    car_models.append(["КАМАЗ", "МАЗ"])
    car_models.append(123)                                          # Лист может содержать элементы любых типов, в том числе дополнительный лист и не один
    print(car_models)
    car_models.extend(["КАМАЗ", "МАЗ"])                             # Корректное добавление элементов одного списка к элементам другого списка
    car_models += ['ГАЗ', 'PORSCHE', 'VW', 'ЛИАЗ']                  # Более удобный способ extend
    #car_models = car_models + ['ГАЗ', 'PORSCHE', 'VW', 'ЛИАЗ']     # Более длинная форма записи
    car_models += ['RENAULT']
    print(car_models)
    print(car_models[0:5])                                          # Слайзинг (нарезка)
    print(car_models[:3])
    print(car_models[5:])
    print(car_models[6:7])
    print(car_models.index('УАЗ'))
    print(car_models.index('УАЗ', 3))
    print(car_models[-3:-1])
    print(list(reversed(car_models)))

    print(car_models)


if __name__ == "__main__":
    main()
