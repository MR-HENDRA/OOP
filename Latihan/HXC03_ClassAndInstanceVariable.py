class Hero:
    #Class Variabel
    jumlah = 0
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        #Instance Variabel
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah += 1
        print("New Hero. My Name is " + inputName)
        
hero1 = Hero("Naruto", 100, 200, 150)
print(Hero.jumlah)
hero2 = Hero("Sazuke", 99, 195, 160 )
print(Hero.jumlah)
hero3 = Hero("Sizuka", 90, 190, 155)
print(Hero.jumlah)