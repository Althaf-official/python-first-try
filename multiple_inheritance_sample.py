class First:
    def display_first(self):
        print("first")

class Second(First):
    def display_second(self):
        print("second")

#now display_first and display_second  going to inherit to another c

class Third(Second):
    def display_third(self):
        print("third")


x=Third()
x.display_third()
x.display_first()
x.display_second()

