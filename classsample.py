class MySampleClass: #this is a class
    def hello(self,n):  #this is a method /function
        self.name=n


    def PrintName(self):
        print("hello"+self.name)

c=MySampleClass()#we assaign MysampleClass as a varibale
name="althaf"
c.hello(name) #we pass the variable here
c.PrintName()