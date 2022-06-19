#in python we can inherit from two class to one class but java cannot
class BaseClass:
    def __init__(self):
        print("Base print")

    def set_name(self,name):
        self.name=name


class Subclass(BaseClass):
    def __init__(self):
        print("subclass init")

    def welcome(self):
        print("welcome")

    def display_name(self):
            print("Name  :"+self.name)#this self.name from the BaseClass


y=Subclass()
y.welcome()

y.set_name("althaf")#now we pass the althaf as a aurgument to self.name then we call this in the display name
y.display_name()