class MySampleClass: #this is a class
    def hello(self,n):  #this is a method /function
        self.name=n


    def PrintName(self):
        print("hello"+self.name)

c=MySampleClass()#we assaign MysampleClass as a varibale
d=MySampleClass()

name="althaf2"
c.hello(name) #we pass the variable here
c.PrintName()

#name="Muhmmed althaf"   - instead of asssign a varible like this directly i pass the value here
d.hello("Muhammed Althaf")
d.PrintName()# i call the function