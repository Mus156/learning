# Tuples - кортежи

def main():
    car_models = ('Audi', 'BMW', "УАЗ")     # Кортеж отличается от списка тем, что доступен только для чтения
    print(car_models)
    print(car_models[0])
    #car_models[0] = 'VW'   - так не получится
    #print(car_models)
    (audi, bmw, uaz) = car_models           # Распаковка кортежа
    print(audi, uaz)
    print(type(car_models))
    car_models_list = list(car_models)      # Преобразуем тип кортеж в тип список
    car_models_list[0] = 'VW'
    car_models = tuple(car_models_list)
    print(type(car_models), car_models)

def people():
    john = ('John', 30, True)
    mary = ('Mary', 20, False)
    family = (john, mary)
    for human in family:                    # Цикл или итерация - поэлементная обработка коллекций (набора элементов/значений)
        (name, age, gender) = human
        print(f'{name} is {"man" if gender else "woman"}. {"Hi" if gender else "She"} is {age}.')     # Тернарный оператор - ответ на вопрос да/нет
        #print(f'{"Hi" if gender else "She"} is {age}.')


if __name__ == "__main__":
    main()
    people()
