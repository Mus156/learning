def main():
    car_models = ['Audi', 'BMW', "УАЗ"]          # В Python это означает список (list), который формируется с помощью []
    print(type(car_models))
    print(len(car_models))
    bmw_is_ok = 'BMW' in car_models              # Оператор in - проверяет наличие элемента в списке
    lada_is_not = 'LADA' not in car_models       # Оператор not in - проверяет отсутствие элемента в списке
    if bmw_is_ok:
        print('BMW входит в список')
    if lada_is_not:
        print('LADA не входит в список')
    car_models.append('LADA')
    car_models = car_models + ['HONDA', 'TOYOTA']
    car_models.insert(100, 'ОКА')
    car_models.insert(80, 'ЗИЛ')
    car_models.remove('ОКА')
    del car_models [5]
    car_models.pop()
    car_models.pop(3)
    car_models = [x for i, x in enumerate(car_models) if i != 2]
    print(car_models)


if __name__ == "__main__":
    main()
