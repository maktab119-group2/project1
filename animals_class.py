from abc import ABC, abstractclassmethod

class animal(ABC):
    def __init__(self,name):
        self.name = name

    @abstractclassmethod
    def talk(self):
        pass
class dog(animal):
    def talk(self):
        return "I am a dog"

class cat(animal):
    def talk(self):
        return "I am a cat"

class horse(animal):
    def talk(self):
        return "I am a horse"
