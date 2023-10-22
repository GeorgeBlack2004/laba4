class House:
    def __init__(self, _area, _price):
        self._area = _area
        self._price = _price

    def final_price(self, discount):
        return self._price * (1 - discount / 100)


class SmallHouse(House):
    def __init__(self, _area, _price):
        super().__init__(_area, _price)
        self._area = 40
        self._price = _price


class Human:
    def __init__(self, w):
        self.wallet = w
        self.house = None

    def make_deal(self, house, _price):
        self.wallet -= _price
        self.house = house

    def buy_house(self, _price):
        if self.wallet < _price:
            return False
        return True


House1 = House(60, 3000)
House2 = House(120, 7000)
SmallHouse1 = SmallHouse(0, 1800)
SmallHouse2 = SmallHouse(0, 1600)
Alexander = Human(5000)
Victoria = Human(3600)
Bob = Human(2000)

deal1 = Bob.buy_house(House1.final_price(10))
if deal1 == 0:
    print("Вы не можете купить этот дом!")
else:
    Bob.make_deal(House1, House1.final_price(10))
    print("Вы купили этот дом! ")
