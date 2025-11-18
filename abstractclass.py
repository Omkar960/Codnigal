from abc import ABC, abstractmethod
class absclass(ABC):
    def print(self,x):
        print("Passed value:",x)
    @abstractmethod
    def task(self):
        print("We are inside the Absclass task")
class test_class(absclass):
    def task(self):
        print("We are test_class task")
testobj = test_class()
testobj.task()
testobj.print(100)

