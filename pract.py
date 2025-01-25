# my_list = [1,2,3,45,6,8]
#
# try:
#     print(my_list[7])
#     print(my_list[0])
# except Exception as e:
#     print("this is exception")
#
# else:
#     print(my_list[2])
#
# finally:
#     print("this is final block")
import copy
# price = 30
# print("price==>",price)
# print(f'{price:.3f}')
# price = 101
# txt = f"It is {'perfect' if price == 100 else 'ok'}"
# print(txt)
# # print('Hello','World')
#
# def srj1(first,second):
#     pass
# def fun(first):
#     print("suraj")
#     return srj(20)
# # print(srj1(100,200))
#
#
# print(srj(10))

# def myfun(num):
#     if num<=1:
#         return num
#     else:
#         return myfun(num-1) + myfun(num-2)
#
#
# for i in range(10):
#     print(myfun(i))

# def fact(n:int):
#     if n==1:
#         return 1
#     else:
#         return n*fact(n-1)
#
# print(fact(5))


# my_list1=[1,2,3,45,6]
# my_list2 = [4,3,56,7,]
#
# print(my_list1+my_list2)
# print(my_list1-my_list2)

# ==============================
import re

# my_string = "my name! i,s suraj"

# fm=re.findall("tu",my_string)

# fm1=re.split(r'\s',my_string)
# print(fm1)


# fm1 = re.split(r'[,.?]', my_string)  # Matches commas, periods, or question marks
# print(fm1)


# my_string = "my, name is! suraj"
#
# temp=re.split(r'[,.,!]',my_string)
# print(temp)
# temp1=re.split(r'\s',my_string)


# year = int(input("user value\n",))
#
# if year%4==0:
#     if year%100==0:
#         if year%400==0:
#             print("its leap year")
#         else:
#             print("its not leap year")
#     else:
#         print("its not leap year")
# else:
#     print("its not leap nyear")
# import copy
# my_list=[[1,2,3],[5,5,6],[7,8,9]]
#
# new_list=copy.copy(my_list)
#
# new_list[0][0]=10
# print(new_list)
# print(my_list)
# import copy
# a = [1,['priya','suraj',['i','j']],3,4]
# b = a
# b = copy.deepcopy(a)
#
# a[1][2]='patil'
# print('a ==>',a)
# print('b ==>',b)


# a=[[1,2,3],[5,6,7],[8,9,0]]
# b=copy.deepcopy(a)
#
# b[0][0]="suraj"
#
# print(a)
# print(b)

# a = int(input("user value\n"))
# print(f"==>{a:,}")

# my_string = [1,2,3,4,5,6,7,7,1]
# uni=[]
# dup=[]
#
# for i in my_string:
#     if i not in uni:
#         uni.append(i)
#     else:
#         dup.append(i)
#
# print(uni)
# print(dup)


# my_string = "suraj"
# reversed_string = ""
# for char in my_string:
#     reversed_string = char + reversed_string
# print(reversed_string)
#
# my_string = [1,2,3,4]
# reversed_string = ""
# for char in my_string:
#     reversed_string = str(char) + reversed_string
# print(reversed_string)

# my_str = "suraj"
# print("".join(reversed(my_str)))

# my_list = [1,2,34,6]
#
# reverse_list = []
# for i in my_list:
#     reverse_list.insert(0, i)
# print(reverse_list)



class Employee:


    def M1(self,*args):
        return sum(args)

    def M1(self,a,b):
        return a+b

object = Employee()
print(object.M1(1,3,7))





















































# try:
#     print("this is try block")
#
# except:
#     print("this is except block")
#
# else:
#     print("this is else block")
#
# finally:
#     print("this is finally block")