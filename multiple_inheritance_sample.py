class First:
    def display(self):
        print("first")

class Second:
    def display(self):
        print("second")

#now display_first and display_second  going to inherit to another c

class Third(First,Second):
    def display_third(self):
        print("third")


x=Third()
x.display_third()
x.display()
