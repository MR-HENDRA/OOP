class Hero:
    
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        
hero1 = Hero("Naruto", 100, 200, 150)
hero2 = Hero("Sazuke", 99, 195, 160 )
hero3 = Hero("Sizuka", 90, 190, 155)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)