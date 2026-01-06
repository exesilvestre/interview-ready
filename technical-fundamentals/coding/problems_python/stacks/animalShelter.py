# 6. *Animal Shelter*#
# An animal shelter, which holds only dogs and cats, operates on a strictly
# "first in, first out" basis. People must adopt either the "oldest"
# (based on arrival time) of all animals at the shelter,
# or they can select whether they would prefer a dog or a cat
# (and will receive the oldest animal of that type).
# They cannot select which specific animal they would like.
# Create the data structures to maintain this system and implement operations
# such as enqueue, dequeueAny, dequeueDog, and dequeueCat.
# You may use the built-in LinkedList data structure.

from typing import Literal


AnimalType = Literal["dog", "cat"]

class Animal:
    def __init__(self, animal_type: AnimalType):
        self.type = animal_type


class AnimalShelter():
    def __init__(self):
        self.dogs: list[Animal] = []
        self.cats: list[Animal] = []
        self.all: list[Animal] = []

    def enqueue(self, type: AnimalType):
        new_animal = Animal(type)
        if type == "dog":
            self.dogs.append(new_animal)
        else:
            self.cats.append(new_animal)
        self.all.append(new_animal)
    
    def dequeueAny(self):
        if not self.all:
            return None
        
        anim = self.all.pop()

        if anim.type == "dog":
            self.dequeueDog()
        else:
            self.dequeueCat()
        return anim

    def dequeueDog(self):
        if not self.dogs:
            return None
        animal = self.dogs.pop()
        for i, a in enumerate(self.all):
            if a.type == "dog":
                self.all.pop(i)
                break
        return animal
    
    def dequeueCat(self):
        if not self.cats:
            return None
        animal = self.cats.pop(0)

        for i, a in enumerate(self.all):
            if a.type == "cat":
                self.all.pop(i)
                break
        
        return animal
    
