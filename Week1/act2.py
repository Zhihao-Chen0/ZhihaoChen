n = int(input("Enter a number to sum even numbers up to: "))
if n < 1:
    print("Invalid number. Please input a number greater than or equal to 1:")

else:
    odd_sum = 0
    even_sum = 0
    i = 1
    print("All even numbers:")
    while i <= n:
        if i % 2 == 0:
            print(i, end=" ")
            even_sum += i
        else:
            odd_sum += i
        i += 1
    print("\nThe sum of even numbers up to", n, "is:", even_sum)
    print("The sum of odd numbers up to", n, "is:", odd_sum)