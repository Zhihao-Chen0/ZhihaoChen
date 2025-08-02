n = int(input("Enter a number to calculate its factorial: "))
if n < 0:
    print("We cannot calculate the factorial of a negative number")

elif 0 <= n <= 1:
    print (1)

else:
    result = 1
    for i in range(1, n + 1):
        result = result * i
    print(result)