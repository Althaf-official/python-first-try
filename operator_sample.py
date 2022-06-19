class sample:
    def set_name(self,name):#now we pass the aurgumet as name
        self.name=name#set the aurgument as self.name

    def __add__(self, other):#call special function for addition
        name=self.name+other.name#this other.name will consider as a second name
        return name



#create object as firstname and second name then call sample on both of them
first_name=sample()
second_name=sample()

#pass the name on the object that we created
first_name.set_name("althaf ")
second_name.set_name("muhammed")


#need come together as althaf muhammed

full_name=first_name+second_name
print(full_name)