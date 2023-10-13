class 붕어빵:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.total = 0

    def sell(self):
        print(f"{self.name}을 {self.money}에 팔았습니다")
        self.total += self.money

    def eat(self):
        print(self.name + "을 먹고있습니다.")


cream = 붕어빵("슈크림", 700)
redbean= 붕어빵("팥", 500)
eggbread =붕어빵("계란빵", 700)

cream.sell()
cream.sell()
redbean.sell()
eggbread.sell()
eggbread.sell()

총판매금액 = (f"{cream.total + redbean.total + eggbread.total}")

print(총판매금액)
