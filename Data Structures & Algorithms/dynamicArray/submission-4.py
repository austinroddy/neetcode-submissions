class DynamicArray:
    
    def __init__(self, capacity: int):
        self.size = capacity
        self.length = 0

        self.dyn_array = [None] * self.size 


    def get(self, i: int) -> int:
        return self.dyn_array[i]   


    def set(self, i: int, n: int) -> None:
        self.dyn_array[i] = n


    def pushback(self, n: int) -> None:
        if self.size == self.length:
            self.resize()
        self.dyn_array[self.length] = n
        self.length += 1


    def popback(self) -> int:
        if self.length > 0:
            self.length -= 1
        return self.dyn_array[self.length]


    def resize(self) -> None:
        self.size = self.size*2
        new_dyn_array = [None] * self.size
        for i in (range(self.length)):
            new_dyn_array[i] = self.dyn_array[i]
        self.dyn_array = new_dyn_array


    def getSize(self) -> int:
        return self.length
    
    
    def getCapacity(self) -> int:
        return self.size