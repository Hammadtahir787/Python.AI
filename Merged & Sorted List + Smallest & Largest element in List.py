list1=[1,5,2,3,6]
list2=[7,9,1,5,4]
list1.sort()
list2.sort()
print("sorted list 1 :",list1)
print("sorted list 1 :",list2)
merge_lists=list1+list2
print("merged and sorted lists :",merge_lists,"\n\n")



smallest_element=merge_lists[0]
Largest_element=merge_lists[-1]
print("The Smallest element of the list is : ",smallest_element)
print("The Largest element of the list is : ",Largest_element)