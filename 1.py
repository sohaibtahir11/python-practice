# temperature = 38.5
# is_vaccinated =False

# if(temperature>37.5 and is_vaccinated==False):
#     print("High fever and not vaccinated — see a doctor immediately")
# elif(temperature>37.5 and is_vaccinated==True):
#     print("High fever but vaccinated — rest at home")
# elif((temperature>36 and temperature<37.5) and is_vaccinated==False ):
#     print("Normal temperature but get vaccinated soon")
# elif((temperature>36 and temperature<37.5) and is_vaccinated==True ):
#     print("All good")
# else:
#     print("Temperature too low — see a doctor")


# fruits = ["Mango","Apple", "Banana", "Watermelon", "Pomegrant"]
# fruits5=[]
# if(len(fruits[0])>5):
#     fruits5.append(fruits[0])
# if(len(fruits[1])>5):
#    fruits5.append(fruits[1])
# if(len(fruits[2])>5):
#    fruits5.append(fruits[2])
# if(len(fruits[3])>5):
#     fruits5.append(fruits[3])
# if(len(fruits[4])>5):
#     fruits5.append(fruits[4])
    
# print(fruits5)



# students = ["Ali", "Sara", "Usman", "Hina", "Bilal"]
# marks = [45, 72, 38, 85, 60]

# if(marks[0]>=50):
#     print(students[0], "Pass")
# else:
#     print(students[0], "Fail")

# if(marks[1]>=50):
#     print(students[1], "Pass")
# else:
#     print(students[1], "Fail")

# if(marks[2]>=50):
#     print(students[2], "Pass")
# else:
#     print(students[2], "Fail")

# if(marks[3]>=50):
#     print(students[3], "Pass")
# else:
#     print(students[3], "Fail")
    
# if(marks[4]>=50):
#     print(students[4], "Pass")
# else:
#     print(students[4], "Fail")


#Question 1
# radius = float(input("Write the radius of the circle: "))
# pi = 3.14

# area = pi*radius*radius
# circumference = 2*pi*radius

# print("Area of the circle is", area)
# print("Circumference of the circle is", circumference)


#Quesiton2
# a = 10
# b = 20

# a,b =b,a
# print (a,b)


 # Question3
# number = int(input("Write any number: "))

# if(number%2==0):
#     Status="Even"
# else:
#     Status="Odd"
# print("Your Number is:",Status)


# Question 4
Age=int(input("Write Your Age: "))

if(0<=Age<=12):
    Status="Child"
elif(13<=Age<=19):
    Status="Teenager"
elif(20<=Age<=59):
    Status="Adult"
elif(59<Age):
    Status="Senior"

print("Your Status is:", Status)
