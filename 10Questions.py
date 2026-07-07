# #Question 1
# radius = float(input("Write the radius of the circle: "))
# pi = 3.14

# area = pi*radius*radius
# circumference = 2*pi*radius

# print("Area of the circle is", area)
# print("Circumference of the circle is", circumference)


# # Quesiton2
# a = 10
# b = 20

# a,b =b,a
# print (a,b)


# #  Question3
# number = int(input("Write any number: "))

# if(number%2==0):
#     Status="Even"
# else:
#     Status="Odd"
# print("Your Number is:",Status)


# # Question 4
# Age=int(input("Write Your Age: "))

# if(0<=Age<=12):
#     Status="Child"
# elif(13<=Age<=19):
#     Status="Teenager"
# elif(20<=Age<=59):
#     Status="Adult"
# elif(59<Age):
#     Status="Senior"

# print("Your Status is:", Status)

# # Question 5
# num1=int(input("write the first number: "))
# num2=int(input("write the second number: "))
# num3=int(input("write the Third number: "))

# if(num1>num2 and num1>num3):
#     print(num1,"is the greatest number!")
# elif(num2>num1 and num2>num3):
#     print(num2,"is the Greatest number!")
# else:
#     print(num3,"is the greatest number!")

# Quesiton 6
year = int(input("write any number: "))

if (year % 4 == 0 and year % 100 != 0):
    print("Its a leap year")
else:
    print("It's not leap year")
