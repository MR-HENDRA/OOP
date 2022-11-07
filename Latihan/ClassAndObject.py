class Hero:
    pass

hero1 = Hero()
hero2 = Hero()
hero3 = Hero();

hero1.name = "Naruto"
hero1.health = 100

hero2.name = "Sazuke"
hero2.health = 99

hero3.name = "Hinata"
hero3.health = 95

print(hero1)
print(hero1.name)
print(hero1.health)
print(hero1.__dict__)

print(hero2)
print(hero2.name)
print(hero2.health)
print(hero2.__dict__)

print(hero3)
print(hero3.name)
print(hero3.health)
print(hero3.__dict__)
