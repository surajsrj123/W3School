
#default arguments
class A:

    def Meth(self,a,b):
        return a+b

    def Meth(self,a,b,c=0):             #c-default argument
        return a+b+c

object = A()
print(object.Meth(5,40))

#variable length arguments


# class Calculator:
#     def add(self, *args):
#         return sum(args)
#
#
# # Example Usage
# calc = Calculator()

# Calling the same method with a variable number of arguments
# print(calc.add(10))            # Output: 10
# print(calc.add(10, 20))        # Output: 30
# print(calc.add(10, 20, 30))    # Output: 60


# method overriding

# class Parent:
#     def A(self):
#         print("this is parent method")
#
# class Child(Parent):
#     def A(self):
#         super().A()    # by using super().we can call parent method
#         print("this is child class")
#
# child=Child()
#
# child.A()








