class House:
    def __init__(self, _area, _price, name):
        self.name = name
        self._area = _area
        self._price = _price

    def final_price(self, discount):
        return self._price * (1 - discount / 100)


class SmallHouse(House):
    def __init__(self, _area, _price, name):
        super().__init__(_area, _price, name)
        self.name = name
        self._area = 40
        self._price = _price


class Human:
    def __init__(self, w, name):
        self.name = name
        self.wallet = w
        self.house = None

    def make_deal(self, house, _price):
        self.wallet -= _price
        self.house = house

    def buy_house(self, _price):
        if self.wallet < _price:
            return False
        return True

    def deal(self, deal, human, house):
        if deal == 0:
            print(f"{self.name} не можете купить этот дом {house.name}!")
        else:
            human.make_deal(house, house.final_price(10))
            print(f"{self.name} может купить этот дом {house.name}! ")


House1 = House(60, 5000, "Beverlie Hills House")
House2 = House(120, 7000, "Hollywood House")

SmallHouse1 = SmallHouse(0, 3000, "Minsk House")
SmallHouse2 = SmallHouse(0, 3000, "Moscow House")

Alexander = Human(10000, "Alexander")
Victoria = Human(3600, "Victoria")
Bob = Human(2000, "Bob")

deal1 = Bob.buy_house(House1.final_price(10))
Bob.deal(deal1, Bob, House1)

deal2 = Victoria.buy_house(SmallHouse1.final_price(20))
Victoria.deal(deal2, Victoria, SmallHouse1)

deal3 = Victoria.buy_house(SmallHouse2.final_price(10))
Victoria.deal(deal3, Victoria, SmallHouse2)

deal4 = Alexander.buy_house(House2.final_price(0))
Alexander.deal(deal4, Alexander, House2)

deal5 = Alexander.buy_house(SmallHouse2.final_price(0))
Alexander.deal(deal5, Alexander, SmallHouse2)
