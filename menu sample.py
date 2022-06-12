menu ={1:'Tea', 2:'Coffe', 3:'Lime', 4:'Shake' }

print(menu)

choice = int(input('Enter your choice: '))

if (choice>4) or (choice<=0) :

    print("invalid Choice")

else :

 print("You have odered: "+menu[choice])