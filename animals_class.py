from abc import ABC, abstractclassmethod

class animal(ABC):
    def __init__(self,name):
        self.name = name

    @abstractclassmethod
    def talk(self):
        pass