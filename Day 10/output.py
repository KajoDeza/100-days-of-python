def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You did not provide valid informaton."

    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"


formated_string = format_name(input("What is your first name? "), input("What is your last name? "))
print(formated_string)



def function_1(text):
    return text + text
output = function_1("hello")
print(output)

def function_2(text):
    return text.title()
output1 = function_1(function_2("hellO"))
print(output1)
