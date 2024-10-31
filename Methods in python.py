#append: List.append
List=[2,4,3,5]
List.append(4)
print(List,"\n")



#Slicing
#Var_name=[Starting_index:Ending_index]
num=[2,5,1,7,8]
numbers=num[1:6]
print(numbers,"\n")




#Sort=Ascending order/Descending order
List=[2,6,3,4,8]
List.sort()
print("This is the Ascending order",List)
List.sort(reverse=True)
print("This is the descending order",List,"\n")


#Sorting method on string
List2=["Orange","Apple","Banana","Mango","Blueberry"]
List2.sort()
print("This is the Ascending order",List2)
List2.sort(reverse=True)
print("This is the descending order",List2,"\n")

#Creating a List
List1=[]
print(len(List1))
List3=[1,2,3,4,5,6,7]
print(len(List3),"\n")

#Reverse
List4=[2,6,3,4,8]
List4.reverse()
print("The reverse order of list is: ",List4,"\n")


#Negative indexing

print("The Last element is: ",List4[-1],"\n")


#insert: first we will add index number and the element which you want to add
List5=["Ali","Ahmed",22,3.4]
List5.insert(1,'Zain')
print("Insert method",List5,"\n")


#Remove:
List5=["Ali","Ahmed",22,3.4]
List5.remove("Ali")
print("Remove method",List5,"\n")

#Pop:
List5=["Ali","Ahmed",22,3.4]
List5.pop(0)
print("Pop Method",List5,"\n")
