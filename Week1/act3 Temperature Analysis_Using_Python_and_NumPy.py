import numpy as np
cel_temps = np.array([18.5, 19, 20, 25.0, 2, 30, 13.9])

average = np.mean(cel_temps)
average = round(average, 1)

maximum = np.max(cel_temps)

minimum = np.min (cel_temps)

print("Average temperture(in Calsius):", average)
print("Maximum temperture(in Calsius):", maximum)
print("Minimum temperture(in Calsius):", minimum)

def change_into_Fahrenheit():
    fah_temps = cel_temps * 9 / 5 + 32
    return fah_temps

fah_temps = change_into_Fahrenheit()
print("The temperature of Fahrenheit is: ", fah_temps)

print("Day with temperatures exceeding 20 degree Calsius: ")

for i, temps in enumerate(cel_temps):
    if(temps> 20):
        print(f"Day{i+1}, {temps}degree Celsius")