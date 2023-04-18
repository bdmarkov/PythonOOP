# from project.cat import Cat
# from project.dog import Dog
# from project.kitten import Kitten
# from project.tomcat import Tomcat
#
# dog = Dog("Rocky", 3, "Male")
# print(dog.make_sound())
# print(dog)
# tomcat = Tomcat("Tom", 6)
# print(tomcat.make_sound())
# print(tomcat)
#
# kitten = Kitten("Kiki", 1)
# print(kitten.make_sound())
# print(kitten)
# cat = Cat("Johnny", 7, "Male")
# print(cat.make_sound())
# print(cat)
from project.animals.birds import Owl, Hen
from project.food import Meat, Vegetable, Fruit

owl = Owl("Pip", 10, 10)
print(owl)
meat = Meat(4)
print(owl.make_sound())
owl.feed(meat)
veg = Vegetable(1)
print(owl.feed(veg))
print(owl)
hen = Hen("Harry", 10, 10)
veg = Vegetable(3)
fruit = Fruit(5)
meat = Meat(1)
print(hen)
print(hen.make_sound())
hen.feed(veg)
hen.feed(fruit)
hen.feed(meat)
print(hen)
