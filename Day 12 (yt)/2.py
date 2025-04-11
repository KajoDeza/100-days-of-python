# x = 1
#
# def outer():
#     x = 2
#     def inner():
#         x = 3
#         print(f"the variable is {x}")
#         return
#     inner()
#     print(f"the variable is {x}")
#     return
# outer()
# print(f"the variable is {x}")

# outcome is 3,2,1
x = 1

# def outer():
#     def inner():
#         print(f"the variable is {x}")
#         return
#     inner()
#     print(f"the variable is {x}")
#     return
# outer()
# print(f"the variable is {x}")

# outcome is 1,1,1

# x = 1
#
# def outer():
#     x = 2
#     def inner():
#         global x
#         x = 3
#         print(f"the variable is {x}")
#         return
#     inner()
#     print(f"the variable is {x}")
#     return
# outer()
# print(f"the variable is {x}")
#
# # the outcome is 3,2,3

x = 1

def outer():
    x = 2
    def inner():
        nonlocal x
        x = 3
        print(f"the variable is {x}")
        return
    inner()
    print(f"the variable is {x}")
    return
outer()
print(f"the variable is {x}")

# nonlocal the one above