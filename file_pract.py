#
# my_dict = {"suraj":"patil","priya":"shegokar",1:"pune",True:"delhi"}
#
# temp= my_dict.update({"suraj":"nerpagar"})
# print(temp)

# my_list = [23,45,65,46]
#
# for i in range(len(my_list)-1):
#
#     for j in range(len(my_list)-1):
#         print('j====',j,end="")
#         if my_list[j]>my_list[j+1]:
#             my_list[j],my_list[j+1]=my_list[j+1],my_list[j]
#
# # print(my_list)
#
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(str(j) * j, end="")
#     print()  # Move to the next line after inner loop


# def fun(n):
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             print(str(j)*j,end="")
#         print()
# fun(5)

#
# def fun(n):
#     for i in range(n,0,-1):
#         for j in range(1,i+1):
#             print(str(j),end="")
#         print()
# fun(5)

# with open("test.txt",'w')as f:
#     print(f.write("this is first test\n"))
#     print(f.write("this is second test\n"))

with open("test.csv",'r')as f:
    print(f.read())
    print(f.read())
















































