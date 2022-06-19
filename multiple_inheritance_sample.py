class First:
    def display_first(self):
        print("first")

class Second:
    def display_second(self):
        print("second")

#now display_first and display_second  going to inherit to another c

class Third(First,Second):
    def display_third(self):
        print("third")


x=Third()
x.display_third()
x.display_second()
x.display_first()
