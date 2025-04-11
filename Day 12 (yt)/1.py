# BUILT IN scopes are python's predefined variables,
# functions, constants, such as print(), return, pass etc.

# GLOBAL scopes are variables that can be  accessed form anywhere in python program

# the LOCAL scope is the code block or body of any Python function

x = 1

def foo():
    global x
    x = 12
    y = 20
    print(f"foo sees y as {x}")
    print(f"foo sees x as {y}")


def bar():
    print(f"bar sees y as {x}")

foo()
bar()
# it's gonna print (x=12 and y=20) but if we add a print function here:

print(f"foo sees y as {x}")

# then it's gonna print the x as 1, to update the global variable with the local one we do this:


