class CrossroadsTeamMember:
    year=2022#this is class variable. class variable commenly one and only
    def __init__(self,name,age,place):
        self.name=name#this is object variable
        self.age=age
        self.place=place

    def add_age(self):
        self.age=self.age+1

    def relocate(self,place):
        self.place = place

    def display(self):
        print("year  :"+str(CrossroadsTeamMember.year))
        print("name  :"+self.name)
        print("age  :"+str(self.age))
        print("place :"+self.place)

    @classmethod #this is way to call class
    def add_year(cls):
        cls.year=cls.year+1

    @staticmethod
    def display_welcome():
        print("welcome")


CrossroadsTeamMember.display_welcome()

x=CrossroadsTeamMember("althaf",26,"kallambalam")
y=CrossroadsTeamMember("muhammed",22,"attingal")



x.display()
y.display()
print("____________________________________________________")

CrossroadsTeamMember.year=CrossroadsTeamMember.year+1

x.add_age()
y.add_age()

#after add year+1
x.display()
y.display()

print("____________________________________________________")
#now we will call class function
CrossroadsTeamMember.add_year()

x.add_age()
y.add_age()

x.display()
y.display()

print("____________________________________________________")
#now we will call class function
CrossroadsTeamMember.add_year()

x.add_age()
y.add_age()
x.relocate("abudhabi")
y.relocate("dubai")

x.display()
y.display()








