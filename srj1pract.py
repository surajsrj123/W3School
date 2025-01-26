my_string = "suraj"
reverse_str = ""
for i in my_string:
    reverse_str = i + reverse_str

print(reverse_str)

my_list = [1,2,3,4,52,67]
reverse_list = ""
for i in my_list:
    reverse_list= str(i) + reverse_list

print(list(reverse_list))

my_list = [1,2,3,4,52,67]
reverse_list=[]
for i in my_list:
    reverse_list.insert(0,i)
print(reverse_list)

