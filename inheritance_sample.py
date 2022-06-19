#in python we can inherit from two class to one class but java cannot
class BaseClass:
    def display(self):
        print("hello")


class Subclass(BaseClass):#here we pass the BaseClass
    def welcome(self):
        print("welcome")

x=BaseClass()
x.display()

y=Subclass()
y.display()
y.welcome()