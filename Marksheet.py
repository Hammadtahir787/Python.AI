a = int(input("Enter the urdu number: "))
b = int(input("Enter the English number: "))
c = int(input("Enter the Maths number: "))
d = int(input("Enter the Science number: "))
e = int(input("Enter the Islamiyat number: "))
f = int(input("Enter the S.st number: "))
g = int(input("Enter the computer number: "))
h = int(input("Enter the French number: "))

sum = a + b + c + d + e + f + g + h

print(f"The obtained Marks are : {sum}")
percentage = sum/800 *100
print(f"The percentage in : {percentage}%")

if percentage >= 80:
    print("A+ Grade")
elif  70 <= percentage < 80:
    print("A Grade")
elif  60 <= percentage < 70:
    print("B Grade")
elif  50 <= percentage < 60:
    print("C Grade")
elif 40 <= percentage < 50:
    print("D Grade")
else:
    print("F Grade")

