class Hero: #Class
    pass

hero1 = Hero() #Object
hero2 = Hero()
hero3 = Hero();

hero1.name = "Naruto"
hero1.health = 100
hero1.power = 200
hero1.armor = 150

hero2.name = "Sazuke"
hero2.health = 99
hero2.power = 195
hero2.armor = 160

hero3.name = "Sizuka"
hero3.health = 90
hero3.power = 190
hero3.armor = 155

print(hero1)
print(hero1.name)
print(hero1.health)
print(hero1.power)
print(hero1.armor)
print(hero1.__dict__)

print(hero2)
print(hero2.name)
print(hero2.health)
print(hero2.power)
print(hero2.armor)
print(hero2.__dict__)

print(hero3)
print(hero3.name)
print(hero3.health)
print(hero3.power)
print(hero3.armor)
print(hero3.__dict__)