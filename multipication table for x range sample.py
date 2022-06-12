value=int(input('enter the number'))
limit=int(input('enter the limit'))
for x in range(1,limit+1):
	print('',x,'x',value,'=',(value*x))
print('FINISHED')



#2nd way

a=int(input("Enter a number: "))

b=int(input("enter the limit"))

print("table of "+ str(a) +" : ")

for x in range(1,b+1):

	res = a*x

	print (str(a)+" * "+str(x)+" = " + str(res))