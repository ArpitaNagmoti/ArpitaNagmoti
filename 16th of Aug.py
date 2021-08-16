#Swap two numbers using temporary variable
x = 30
y = 10

temp = x
x = y
y = temp

print("The value of x after swapping: ",(x))
print("The value of y after swapping: ",(y))

#Find ASCII value of a character 'X' 'x'
A='X'
N='x'
print("The ASCII value of A is",ord(A))

print("The ASCII value of N is",ord(N))

#write a program to compute quotient and remainder
x,y=divmod(10,20)
print("\nquotient of : ",x)
print("\nremainder of :",y)

#Write Program to Check Whether a Number is Even or Odd

num = int(input("\nEnter a number: "))
if (num % 2) == 0:
   print("\n{0} is Even".format(num))
else:
   print("\n{0} is Odd".format(num))


 #check whether an alphabet is vowel or constant using if..else statement - a,b,e,o
l= input("\n Enter a charater")

if l in ('a','e','o'):
        print("\n %s is a vowel."%l)
else:
        print("\n %s is a constant."%l)





