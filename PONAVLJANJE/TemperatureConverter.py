print("Welcome to the Temperature Converter")

def convert_temperature(value, unit):
    if unit == "F":
        return (value - 32) * 5/9
    elif unit == "C":
        return (value * 9/5) + 32
    else:
        print("Invalid unit")

print(convert_temperature(98.6, "F"))
