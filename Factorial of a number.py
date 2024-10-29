num = int(input("Enter the number:"))
fact = 1
a = 1
while a<=num:
    fact = fact * a
    a=a+1
print(f"The factorial of {num} is {fact}")