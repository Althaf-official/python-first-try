import datetime
now=datetime.datetime.now()

print(now.strftime("%d:%m:%Y"))
print(datetime.datetime.today())


#how to add data from
x=datetime.datetime(year=2020,day=4,month=12)
y=datetime.datetime(year=2020,day=4,month=10)

dif=x-y
print(dif)

print(x)

#now we will the difference between this project starting time and ending time
end=datetime.datetime.now()
difference=end-now
print(difference)#its showing micro seconds