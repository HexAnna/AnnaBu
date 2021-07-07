# Пыталась сделать доску обьвлений, но не совсемпродумала как
# соединить под классы Продавец/покупатель с Классом обьявления, т.к. в нем подклассы были (транспорт, мебель и т.д.)
# Через мнодественное наследование хотела по пробовать сдеть, но не рабобралась как.
class Person:
    def __init__(self):
        self.name = 'User'
        self.surname = 'User Surname'
        self.telephone_number = 8800

    def show_info(self):
        print(self.name, self.surname, self.telephone_number)


p = Person()
p.show_info()


class Ads:
    def __init__(self):
        self.ads_number = 1

    def your_number(self, ads_number):
        print(self.ads_number+1)

ads = Ads()
ads.your_number(1)


class Seller(Person, Ads):
    def __init__(self, name, text):
        Person.__init__(self)
        self.text = text
        self.name = name

    def sale(self):
        print('Hello. My name is', self.name, 'I\' want sale this', self.text)


class Buyer(Person):
    def __init__(self, name, surname, text):
        Person.__init__(self)
        self.text = text
        self.name = name
        self.surname = surname

    def buy(self):
        print('Hello. My name is', self.name, self.surname,
              'I\' want buy this', self.text, '. You can call my on ', self.telephone_number)


my_sale = Seller('Bob', 'car')
my_sale.sale()
my_buy = Buyer('Mike', 'Miers', 'Table')
my_buy.buy()
