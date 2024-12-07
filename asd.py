import random

class Human:
    def __init__(self, name="Human"):
        self.name = name
        self.money = 100
        self.happiness = 50
        self.hunger = 50
        self.food = 50
        self.car_fuel = 100
        self.house_mess = 0

    def eat(self):
        if self.food > 0:
            print(f"{self.name} поел.")
            self.hunger += 10
            self.food -= 10
        else:
            print(f"У {self.name} нет еды! Нужно купить.")

    def work(self):
        print(f"{self.name} пошел работать.")
        self.money += 50
        self.happiness -= 5
        self.hunger -= 5
        self.car_fuel -= 10

    def relax(self):
        print(f"{self.name} отдыхает.")
        self.happiness += 10
        self.house_mess += 5

    def clean(self):
        print(f"{self.name} убрался в доме.")
        self.house_mess = 0
        self.happiness -= 5

    def shop(self, item):
        if item == "food":
            print(f"{self.name} купил еду.")
            self.food += 30
            self.money -= 30
        elif item == "fuel":
            print(f"{self.name} купил бензин.")
            self.car_fuel += 50
            self.money -= 50

    def status(self):
        print(f"\nДень {day}. Жизнь {self.name}:")
        print(f"Деньги: {self.money}, Счастье: {self.happiness}, Сытость: {self.hunger}")
        print(f"Еда дома: {self.food}, Бензин: {self.car_fuel}, Беспорядок: {self.house_mess}")

    def live(self):
        self.status()
        if self.hunger < 20:
            self.eat()
        elif self.car_fuel < 20:
            self.shop("fuel")
        elif self.money < 0:
            self.work()
        elif self.house_mess > 20:
            self.clean()
        else:
            action = random.choice(["work", "relax", "shop"])
            if action == "work":
                self.work()
            elif action == "relax":
                self.relax()
            elif action == "shop":
                self.shop("food")
        if self.happiness <= 0 or self.hunger <= 0 or self.money < -100:
            print(f"{self.name} не смог дальше жить...")
            return False
        return True
    def communication(self):
        if action =="communication":
            print(f"{self.name} общается с другом.")
            self.happiness += 10
            self.hunger -= 5
            self.car_fuel -= 5
nick = Human(name="Ник")

for day in range(1, 150):  # Симуляция 7 дней
    if not nick.live():
        break
