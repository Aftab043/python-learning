num = [1,2,3,4,5,6,2]
print(num.append(10), "add / append number in end :" , num) # adds one element at the end [1, 3, 4, 5, 6, 2, 10]
print(num.sort(), "sort ascending order :" , num) # sorts in sacending order [1, 2, 3, 4, 5, 6, 10]
print(num.sort(reverse=True), "sort descending order :" , num) # sorts in descending order [10, 6, 5, 4, 3, 2, 1]
print(num.reverse(), "reverse number :" , num) # reverse list [1, 2, 3, 4, 5, 6, 10]
print(num.insert(2, 0), "insert number :" , num) # insert element at idx [1, 2, 0, 3, 4, 5, 6, 10]
print(num.remove(2), "removes first occurrence of element [1,2,3,4,5,6,2] :" , num) # [1, 0, 2, 3, 4, 5, 6, 10]
print(num.pop(6), "removes element at index [1,2,3,4,5,6,2] :" , num) # [1, 0, 2, 4, 5, 6, 10]
 