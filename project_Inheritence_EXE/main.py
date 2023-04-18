from project_Inheritence_EXE.food import Food
from project_Inheritence_EXE.product_repository import ProductRepository
from project_Inheritence_EXE.drink import Drink

food = Food("apple")
drink = Drink("water")
repo = ProductRepository()
repo.add(food)
repo.add(drink)
print(repo.products)
print(repo.find("water"))
repo.find("apple").decrease(5)
print(repo)
