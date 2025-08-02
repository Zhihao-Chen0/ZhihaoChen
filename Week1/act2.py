n = int(input("Enter a number to sum even numbers up to: "))
if n < 0:
    print("We cannot calculate the factorial of a negative number")

elif 0 <= n <= 1:
    print (0)

else:
    result = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            result = result + i
    print("The sum of even numbers up to", n, "is:", result)