age_year = int(input("What year were you born? "))
this_year = 2025
print(f"You are: {this_year - age_year} years old")

age = this_year - age_year

if age > 18:
    print("You are an adult")
else:
    print("You are a minor")
