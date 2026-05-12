class Dog():
    animal_type = "Dog"
    species = ["Golden Retriever", "Labradour", "Chihuahua", "Mutt"]
    def __init__(self, name, age, species, colour, hair_type, personality):
        self.name = name
        self.age = age
        self.species = Dog.species[species]
        self.colour = colour
        self.hair_type = hair_type
        self.personality = personality
    def bark_name(self):
        print(self.name + "! Bark Bark!")

tommy = Dog("Tommy", 20, 1, "Black", "Long", "Friendly")
print(tommy.name, tommy.age , tommy.personality, tommy.species)

tommy.bark_name()