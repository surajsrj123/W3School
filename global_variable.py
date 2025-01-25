
# x=10             #  global variable
# def srj():
#     global x
#     x=20          #   update global variable as x=20
# srj()         # call global x
# print(f"print x value={x}")  # it will print 20


# x=10
# def srj():
#     x=20
# srj()
# print(x)    # it will print 10

# [print(x) for x in ['apple', 'banana', 'cherry']]

# my_list = [1,23,4,5]
# [print(i)for i in my_list]
#
# # for i in my_list:
# #     print(i,end=" ")

fruits = ['apple', 'banana', 'cherry']
newlist = [x for x in fruits if x == 'banana']
print(newlist)
# mewlist= ['orange' if i=='apple' else i for i in fruits]
# print(mewlist)
# [print(i) for i in fruits]
# newlist = [x for x in fruits if x == 'banana']

# fruits = ['apple', 'banana', 'cherry']
# newlist = ['orange' if x == 'banana' else x for x in fruits ]


# my_list = ["suraj","priya"]
#
# temp=[i for i in my_list if i =="priya" ]
# print('temp ===>',temp)

# fruits = ['apple', 'banana', 'cherry']
# newlist = ['apple' for x in fruits]
# print(newlist)

# fruits = ('apple', 'banana', 'cherry')
# (x, y, z) = fruits
# print(y)

# fruits = ('apple', 'banana', 'cherry')
# (x, *y) = fruits
# print(y)

# my_list = (1,2,3,4)
#
# i=0
# while i<len(my_list):
#     print(my_list(i))
#     i=i+1

# mytuple = ['apple', 'banana', 'cherry']
# print(mytuple[0])
# print(mytuple[1])
# print(mytuple[2])
# i = 0
# while i < len(mytuple):
#
#   i = i + 1

# thisset = {'apple', 'banana', 'cherry'}
# print('banana' not in thisset)

# fruits = {"apple", "banana", "cherry"}
# more_fruits = ["orange", "mango", "grapes"]
# temp=fruits.update(more_fruits)
# # print(fruits)
# # temp=fruits.add(more_fruits)
# print(fruits)

# class Employee:
#     def __init__(self,first):
#         self.firstnum=first
#     def __str__(self,second):
#         self.secondnum=second
#
#
#     def srj(self):
#         return self.firstnum
#     def pri(self):
#         return self.secondnum
#
#
#
# object = Employee(100)
# print(object.srj())
# print(object.pri())














































