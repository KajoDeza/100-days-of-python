import random


def my_function(my_list):
    random_name = random.choice(my_list)
    print(random_name.title())


my_function(my_list = ["angela", "john", "mark", "anne", "DiAna", "ErnesTo", "LAYLA"])