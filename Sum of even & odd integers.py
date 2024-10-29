numbers=map(int,input("Enter the integer seperated by spaces:").split())
sum_even=0
sum_odd=0
for num in numbers:
    if num%2==0:
        sum_even+=num
    else:
        sum_odd+=num
print(f"The sum of even integers are : {sum_even}")
print(f"The sum of odd integers are : {sum_odd}")