class Magnit():
    def __init__(self, name, specialization):
        self.name = name
        self.type = specialization

    def show_info(self):
        print(self.name, self.type)


class Saller(Magnit):
    def __init__(self, name, sale):
        self.name = name
        self.sale = sale
        self.next = None

    def welcome(self):
        print('Hello. How can I help you?'.format())
        self.show_goods()
        self.next = input('You have chosen something?')
        if self.next in self.sale:
            print(self.next and self.sale[self.next])
        else:
            print('Want to add something else?')

    def show_goods(self):
        print(self.sale)


class Buyer():
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet


sale = {'Cosmetics': 1, 'Food': 2, 'Food for animals': 3, 'Goods for kids': 4, 'Household ': 5}
saller = Saller("Sisi", sale)

saller.welcome()
