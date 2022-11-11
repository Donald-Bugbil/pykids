from .container import Container

class StringContainer(Container):

    """doc for working with string containers"""

    def __init__(self, *args):
        self._items = args
        self._arr = []
        for item in self._items:
            self._arr.append(item)
    
    def __add__(self, other):
        return StringContainer(','.join(self._arr + other._arr))

    #overriding all_items_method
    def add_all_items(self):
        concat = ''
        for item in self._items:
            concat = concat + item
        return concat

    def __str__(self):
        long_name = ''
        for item in self._items:
            long_name = long_name + item + ' '
        return long_name
    
    #overriding list_items method
    def list_items(self):
        for item in self._items:
            print(item)
    
    
    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self._arr):
            result = self._arr[self.index]
            self.index = self.index + 1
            return result
        else:
            raise StopIteration
        

    
