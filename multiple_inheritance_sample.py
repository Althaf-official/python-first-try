class First:
    def display_first(self):
        print("first")

class Second(First):#inheritted from the first class
    def display_second(self):
        print("second")

#now display_first and display_second  going to inherit to another c

class Third(Second):#inherit from the sencond class
    def display_third(self):
        print("third")


x=Third()
x.display_third()
x.display_first()
x.display_second()

