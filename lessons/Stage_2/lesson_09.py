
name = "Danny"
age = 37

concatenate = "Hi, my name is " + name + ". I am " + str(age) + " years old"
print(concatenate)

f_string = f"Hi, my name is {name}. I am {age} years old"
print(f_string)

print(f"HI, my name is {name.upper()}. I am {age-2} years old")

format_string = "Hi, my name is {}. I am {} years old".format(name, age)
print(format_string)

assert concatenate == f_string
assert f_string == format_string
assert format_string == concatenate

