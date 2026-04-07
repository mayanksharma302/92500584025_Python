from abc import ABC, abstractmethod

class a(ABC):

    @abstractmethod
    def sound(self):
        pass


class b(a):

    def sound(self):
        print("this is b method")


d = b()
d.sound()
