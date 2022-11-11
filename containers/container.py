from abc import ABC, abstractmethod

class Container(ABC):

    @abstractmethod
    def add_all_items(self):
        pass

    @abstractmethod
    def list_items(self):
        pass
    