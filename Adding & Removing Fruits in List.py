list=["Apple","Mango","Grapes","Banana"]
print(list)
insert_fruit=input("Add the fruit to the list:\n").capitalize()
list.append(insert_fruit)
remove_fruit=input("Remove the fruit from the list :\n").capitalize()
list.remove(remove_fruit)
print("Updated List is :",list)