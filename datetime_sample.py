import datetime
now=datetime.datetime.now()

print(now.strftime("%d:%m:%Y"))
print(datetime.datetime.today())


#how to add data from
x=datetime.datetime(2020,4,12)
y=datetime.datetime(2015,4,12)

dif=x-y
print(dif)

print(x)