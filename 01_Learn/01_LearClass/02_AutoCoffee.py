class AddMixin():
    # 此类为添加东西的类
    def addliquid(self, liquid, nums, temp):
        # 此方法用于加液体
        self.liquid = liquid
        self.volume = nums
        if temp == "cold":
            self.temperature = "cold"
        elif temp == "hot":
            self.temperature = "hot"
        return f"add {self.temperature} {self.liquid} {self.volume} ML"


class Coffee(AddMixin):
    # 此类为咖啡
    def __init__(self, water=1, water_temp="hot", milk=1, milk_temp="hot", coffee=1, coffee_temp="hot"):
        self.water = water
        self.water_temp = water_temp
        self.milk = milk
        self.milk_temp = milk_temp
        self.coffee = coffee
        self.coffee_temp = coffee_temp
        self.prescription = []

        if int(self.water) > 0:
            self.prescription.append(super().addliquid("water", self.water, self.water_temp))

        if int(self.milk) > 0:
            self.prescription.append(super().addliquid("milk", self.milk, self.milk_temp))

        if int(self.coffee) > 0:
            self.prescription.append(super().addliquid("coffee", self.coffee, self.coffee_temp))

    def showPrescription(self):
        for i in self.prescription:
            print(i)


# 实例化一杯拿铁
latte = Coffee(water=50, water_temp="hot", milk=300, milk_temp="hot", coffee=150, coffee_temp="hot")
latte.showPrescription()
