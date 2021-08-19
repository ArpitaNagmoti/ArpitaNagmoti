# 1.Reverse a String and print it on console"Python Skills" 
str = "Python Skills"

print("Before reversing string: " + str)

str = str[::-1] 

print("After reversing string: " + str)

# 2.Assign String to x variable in DD-MM-YYYY format extract and print Year from String
import datetime
x = "19-08-2021" 
format = "%d-%m-%Y"

dt_object = datetime.datetime.strptime(x, format)

print("Year: ", dt_object.year)


# 3.In a small company, the average salary of three employees is Rs1000 per week. If one employee earns Rs1100 and other earns Rs500, how much will the third employee earn? Solve by using java programm
e1=1100
e2=500
e3=0
avg=1000

totalsalaryof3emp=1000*3

e3=totalsalaryof3emp-e1-e2

print("Salary of third employee is ",e3)

# 4.Write Program - convert a percentage to a fraction (To convert a percentage into fraction let say 30% to a fraction)
per = 30

frac = per / 100

print ("Fraction of 30% is:")
print(frac)

# 5.Write Program - A train 340 m long is running at a speed of 45 km/hr. what time will it take to cross a 160 m long tunnel?
tunneld=160

speed=45000/3600

distance=340+160

time=distance/speed

print("time required to cross a tunnel is ",time)
