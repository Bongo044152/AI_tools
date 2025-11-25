from abc import ABC, abstractmethod

class BaseToolModel(ABC):
    @abstractmethod
    def use(self):
        pass
    
    @abstractmethod
    def show(self):
        pass