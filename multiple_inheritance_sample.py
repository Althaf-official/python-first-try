class First:
    def display(self):
        print("first")

class Second():
    def display(self):
        print("second")

class Third(Second,First):#(First,Second))  it will show the result from left to right .means if you make the argument second it will show the function second firstly
    def display1(self):
        print("third")
#this case it will only search until found.

x=Third()
x.display()

print(Third.mro())

#now the Class name Second comes first

