import numpy as np
rainfall = np.array([0.0, 5.2, 3.1, 0.0, 12.4, 0.0, 7.5])

total = round(np.sum(rainfall), 1)
average = round(np.mean(rainfall), 1)

print(f"Total rainfall: {total}mm")
print(f"Average rainfall: {average}mm")

count = 0
for i, value in enumerate(rainfall):
    if value == 0:
        count += 1
    
print("Total no-rain days: ", count)

print("Days with rainfall over 5mm:")
for i, value in enumerate(rainfall):
    if value > 5:
        print(f"Day{i}(index): {value}mm")
