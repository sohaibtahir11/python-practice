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


fruits = ["Mango","Apple", "Banana", "Watermelon", "Pomegrant"]
fruits5=[]
if(len(fruits[0])>5):
    fruits5.append(fruits[0])
if(len(fruits[1])>5):
   fruits5.append(fruits[1])
if(len(fruits[2])>5):
   fruits5.append(fruits[2])
if(len(fruits[3])>5):
    fruits5.append(fruits[3])
if(len(fruits[4])>5):
    fruits5.append(fruits[4])
    
print(fruits5)