def main():
    car_models = {'Audi', 'BMW', 'BMW', 'BMW', 'BMW', "УАЗ", None}     # Set - отличается от списка тем, что может содержать только уникальные значения
    print(car_models)                                                  # В set нет гарантированного порядка элементов
    print(type(car_models))
    people = {'Jonh', 'Mary', None}
    print(car_models | people)                                         # Обьединение set-ов
    print(car_models.union(people))                                    # Обьединение set-ов
    print(car_models.union(['ОКА', "ОКА", "КАМАЗ"]))                   # Обьединение типа set и типа list



if __name__ == "__main__":
    main()
