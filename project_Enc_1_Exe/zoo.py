from project_Enc_1_Exe.caretaker import Caretaker
from project_Enc_1_Exe.cheetah import Cheetah
from project_Enc_1_Exe.keeper import Keeper
from project_Enc_1_Exe.lion import Lion
from project_Enc_1_Exe.tiger import Tiger
from project_Enc_1_Exe.vet import Vet


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget >= price and len(self.animals) < self.__animal_capacity:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {type(animal).__name__} added to the zoo"
        if len(self.animals) < self.__animal_capacity and self.__budget < price:
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {type(worker).__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker.name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salaries = sum(map(lambda worker: worker.salary, self.workers))

        if total_salaries <= self.__budget:
            self.__budget -= total_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_money = sum(map(lambda animal: animal.money_for_care, self.animals))

        if total_money <= self.__budget:
            self.__budget -= total_money
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit_amount(self, amount):
        self.__budget += amount
        return self.__budget

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"

        lions_info = []
        for animal in self.animals:
            if type(animal) == Lion:
                lions_info.append(repr(animal))

        tiger_info = []
        for animal in self.animals:
            if type(animal) == Tiger:
                tiger_info.append(repr(animal))

        cheetah_info = []
        for animal in self.animals:
            if type(animal) == Cheetah:
                cheetah_info.append(repr(animal))

        result += f"----- {len(lions_info)} Lions:\n"
        lions_result = '\n'.join(lions_info)
        result += lions_result + '\n'

        result += f"----- {len(tiger_info)} Tigers:\n"
        tiger_result = '\n'.join(tiger_info)
        result += tiger_result + '\n'

        result += f"----- {len(cheetah_info)} Cheetahs:\n"
        cheetah_results = '\n'.join(cheetah_info)
        result += cheetah_results

        return result

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"

        keepers_info = []
        for worker in self.workers:
            if type(worker) == Keeper:
                keepers_info.append(repr(worker))

        vet_info = []
        for worker in self.workers:
            if type(worker) == Vet:
                vet_info.append(repr(worker))

        caretaker_info = []
        for worker in self.workers:
            if type(worker) == Caretaker:
                caretaker_info.append(repr(worker))

        result += f"----- {len(keepers_info)} Keepers:\n"
        keepers_result = '\n'.join(keepers_info)
        result += keepers_result + '\n'

        result += f"----- {len(caretaker_info)} Caretakers:\n"
        caretaker_results = '\n'.join(caretaker_info)
        result += caretaker_results + '\n'

        result += f"----- {len(vet_info)} Vets:\n"
        vet_results = '\n'.join(vet_info)
        result += vet_results



        return result