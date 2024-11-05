Birthdays={"Suleman":"10th October",
           "Zayam":"9th November",
           "Abdul Basit":"22nd January"
           }
for name in Birthdays:
    print(name)
name=input("Enter the name of person from above mentioned name whose birthday you want to know:").capitalize()
if name in Birthdays:
    print(name,"'s birthday is on",Birthdays[name])
else:
    print("The person is not in the list!")