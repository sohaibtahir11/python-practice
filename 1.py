temperature = 38.5
is_vaccinated =False

if(temperature>37.5 and is_vaccinated==False):
    print("High fever and not vaccinated — see a doctor immediately")
elif(temperature>37.5 and is_vaccinated==True):
    print("High fever but vaccinated — rest at home")
elif((temperature>36 and temperature<37.5) and is_vaccinated==False ):
    print("Normal temperature but get vaccinated soon")
elif((temperature>36 and temperature<37.5) and is_vaccinated==True ):
    print("All good")
else:
    print("Temperature too low — see a doctor")