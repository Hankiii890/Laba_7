def delivery(func):
    def wrapper(num_items):
        import time
        print(f'Время запуска функции: {time.time()}')
        print(f"Колличесво товаров: {num_items}")
        result = func(num_items)
        print(f"Стоимость доставки: {result}")
        return result
    return wrapper

@delivery
def shop(quantity_of_goods):
    if quantity_of_goods == 1:
        return 10.95
    elif quantity_of_goods < 1:
        return 0
    else:
        return 10.95 + (quantity_of_goods - 1) * 2.95

num_items = int(input("Введите кол-во товаров: "))
shop(num_items)
