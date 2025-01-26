
my_list = [1,23,4,6,2,7,6,78]

temp=my_list.sort(reverse=True)
print(my_list)

# without inbuilt

my_list = [1,23,5,6,54,67]

for i in range(len(my_list)-1):
    for j in range(len(my_list)-1):
        if my_list[j]>my_list[j+1]:
            my_list[j],my_list[j+1]=my_list[j+1],my_list[j]

print(my_list)
print(my_list[::-1])