# #return
# def fun():
#     s = 0
#     for i in range(10):
#         s += 1
#         return s
# print(fun())
# #yeild
#
# def fun():
#     s = 0
#     for i in range(10):
#         s += 1
#         return s
# print()
#
# # t=[1,2,3,4]
# # t[1:-1]
#
# def main():
#     print('hello')
#     print('world')
#     print('before')
# main()
# print('after')
#
#
# #
# na = "harish"
# na = na[1:6].replace("h", "t")
# # print(na)
# def adone(num):
#     return num + 1
# adone(7)


# def the_outer_function():
#     var = 10
#
#     def the_inner_function():
#         global var
#         var = 14
#         print("The value inside the inner function: ", var)
#
#     the_inner_function()
#     print("The value inside the outer function: ", var)
#
#
# the_outer_function()
# print(var)
#
# l=(1,2,[3,4])
# l[2].insert(1,'a')
# print(l)
import copy
l=[1,2,3,[4,5],6]
l1=copy.deepcopy(l)
print(l)
print(l1)
print(id(l))
print(id(l1))
l1.insert(2,2)
print(l)
print(l1)
l1[4][1]=44444
print(l)
print(l1)
print(id(l))
print(id(l1))
