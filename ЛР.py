# Модель
class Equipment:
    checklistTV = []

    def equipment_method(self):
        print("")


class Worker:
    def worker_method(self):
        print("")


class Manager(Worker):
    # атрибуты
    name = "Bob"
    post = "Главный менеджер"

    # методы
    def hello(self):
        print()
        print('*********************************')
        print('* Приветсвуем вас в нашем магазине " *')
        print('*********************************')
        print()

    def get_inf(self):
        print('Меня зовут', self.name)
        print('Я', self.post)
        print()

    def set_manager(self, name, post):
        self.name = name
        self.post = post

    @staticmethod
    def write_inf():
        print("Как вас зовут")
        client_name = input()
        return client_name

    @staticmethod
    def ask_about_equipment():
        print('Что вы хотели купить? Введите число: 1 - телевизоры, 2 - микроволновки, 3 - ноутбуки, '
              '4 - принтеры, 5 - мониторы (работает для телевизоров, пока что)')
        client_equipment = int(input())
        if client_equipment == 1:
            print('{: <8} | {: >8}'.format("Модель", "Цена"))
            i = 0
            while i < Equipment.checklistTV.__len__():
                print('{: <8} | {: >8}'.format(Equipment.checklistTV[i], Equipment.checklistTV[i + 1]))
                i = i + 3

    def ask_about_model(self):
        print("Какая модель вас интересует(введите номер строки): ")
        interesting_model = int(input())
        if Equipment.checklistTV[interesting_model*3 - 1] == "Da":
            print("Продано")
        elif interesting_model*3 - 1 > Equipment.checklistTV.__len__():
            print("Данной строки нет")
        else:
            print("Данной модели нет :(")
            print()


class Customer:
    # атрибуты
    name = "Bob"
    TV = ''
    microwave = ''
    laptop = ''
    monitor = ''
    printer = ''

    # методы
    def get_name(self):
        print(self.name)

    def set_TV(self, TV):
        self.TV = TV

    def set_laptop(self, laptop):
        self.laptop = laptop

    def set_microwave(self, microwave):
        self.microwave = microwave

    def set_printer(self, printer):
        self.printer = printer

    def set_TV(self, TV):
        self.TV = TV

    def set_name(self, name):
        self.name = name

    def get_TV(self):
        print(self.TV)


class TV(Equipment):
    model = ""
    price = ""
    serviceability = ""

    def __init__(self, model, price, serviceability):
        self.model = model
        self.price = price
        self.serviceability = serviceability
        self.checklistTV.append(self.model)
        self.checklistTV.append(self.price)
        self.checklistTV.append(self.serviceability)

    def set_model(self, model):
        self.model = model

    def set_price(self, price):
        self.price = price

    def set_serviceability(self, serviceability):
        self.serviceability = serviceability

    def choose_TV(self, choose_TV):
        pass


class microwave(Equipment):
    model = ""
    price = ""
    serviceability = ""

    def __init__(self, model, price, serviceability):
        self.model = model
        self.price = price
        self.serviceability = serviceability

    def set_model(self, model):
        self.model = model

    def set_price(self, price):
        self.price = price

    def set_serviceability(self, serviceability):
        self.serviceability = serviceability

    def choose_microwave(self, choose_TV):
        pass


class laptop(Equipment):
    model = ""
    price = ""
    serviceability = ""

    def __init__(self, model, price, serviceability):
        self.model = model
        self.price = price
        self.serviceability = serviceability

    def set_model(self, model):
        self.model = model

    def set_price(self, price):
        self.price = price

    def set_serviceability(self, serviceability):
        self.serviceability = serviceability

    def choose_laptop(self, choose_TV):
        pass


class printer(Equipment):
    model = ""
    price = ""
    serviceability = ""

    def __init__(self, model, price, serviceability):
        self.model = model
        self.price = price
        self.serviceability = serviceability

    def set_model(self, model):
        self.model = model

    def set_price(self, price):
        self.price = price

    def set_serviceability(self, serviceability):
        self.serviceability = serviceability

    def choose_laptop(self, choose_TV):
        pass


class monitor(Equipment):
    model = ""
    price = ""
    serviceability = ""

    def __init__(self, model, price, serviceability):
        self.model = model
        self.price = price
        self.serviceability = serviceability

    def set_model(self, model):
        self.model = model

    def set_price(self, price):
        self.price = price

    def set_serviceability(self, serviceability):
        self.serviceability = serviceability

    def choose_monitor(self, choose_TV):
        pass

LG = TV("Lg", 1200, "Da")
Samsung = TV("Samsung", 1200, "No")
Sony = TV("Sony", 1200, "No")
manager = Manager()
customer = Customer()
manager.hello()
manager.get_inf()
customer.name = manager.write_inf()
manager.ask_about_equipment()
manager.ask_about_model()