class Pet:
    def __init__(self, name, health):
        self.name = name
        self.__health = health  # Private health data

    def get_health(self):
        return self.__health

    def set_health(self, new_health):
        if 0 <= new_health <= 100:
            self.__health = new_health
        else:
            print("Invalid health value!")

    def show_care(self):
        print(self.name, "needs food, water, and care.")


class Dog(Pet):
    def show_care(self):
        print(self.name, "needs walks and healthy dog food.")


class Cat(Pet):
    def show_care(self):
        print(self.name, "needs a clean litter box and cat food.")


class Rabbit(Pet):
    def show_care(self):
        print(self.name, "needs fresh hay and a safe space.")



pets = [
    Dog("Buddy", 90),
    Cat("Whiskers", 85),
    Rabbit("Coco", 95)
]

print("===== MY PET CARE DASHBOARD =====")

for pet in pets:
    print("\nPet Name:", pet.name)
    print("Health:", pet.get_health(), "/ 100")
    pet.show_care()  # Polymorphism


print("\n===== HEALTH UPDATE =====")
pets[0].set_health(95)
print("Buddy's updated health:", pets[0].get_health())
