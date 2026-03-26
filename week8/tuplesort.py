print("Sorting List of Tuples Based on Last Element")
lst=[(1,3),(4,1),(2,5),(6,0)]
print("The original list is:",lst)
sorted_lst=sorted(lst,key=lambda x:x[-1])
sorted_tuple=tuple(sorted_lst)
print("The sorted tuple is:",sorted_tuple)