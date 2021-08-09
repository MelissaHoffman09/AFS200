# Manipulate String

name = input("Enter your name: ")
age = input("Enter your age: ")
current_year = 2021
age = int(age)
diff_years = 100 - age
age_100 = current_year + diff_years

print(name, "will turn 100 years old in", diff_years, "years from now; in the year", age_100)