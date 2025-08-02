n = int(input("Enter a number to sum even numbers up to: "))
if n < 1:
    print("In valid number. Please input a number over or equal than 1:")

else:
    result = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            result = result + i
    print("The sum of even numbers up to", n, "is:", result)