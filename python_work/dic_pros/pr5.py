# Q1
def append_to_list(lst, number):
    lst.append(number)
    return lst


lst = list(map(int,input("Enter the number sequence: ").split()))
number = int(input("Enter the number to append: "))
print(append_to_list(lst,number))

# # Q2
# [1,2,3]
#
# [1,2,3,4]

# Q3
data = [10, 20, 30, 40]
data.clear()
print(data)

#Q4
Answer : 3

#Q5
def extend_list(list1, list2):
    list.extend(list2)
    return list1

list1 = [1,2,3,4]
list2 = [5,6]
print(extend_list(list1,list2))    # [1,2,3,4,5,6]

#Q6
nums = [4, 5, 7, 8, 7, 9]
# Write the code to find index of first 7
index_value = nums.index(7)
print(index_value)      # 2

#Q7
my_list = [10, 20, 30, 40]
my_list.insert(2,100)
print(my_list)             # [10,20,100,30,40]

#Q8
a = [9, 8, 7]
x = a.pop()
print("Popped:", x)          # 7
print("Remaining:", a)      # [9,8]

#Q9
fruits = ["apple", "banana", "apple", "cherry"]
fruits.remove("apple")
print(fruits)             # ["banana", "apple", "cherry"]

#Q10
nums = [1, 2, 3, 4, 5]
nums.reverse()
print(nums)          #[5,4,3,2,1]

# Q11
grades = [88, 75, 92, 85]
grades.sort()
print(grades)        # [75,85,88,92]
grades.sort(reverse=False)
print(grades)       # [92,88,85,75]








