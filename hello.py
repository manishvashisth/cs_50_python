# comments, pseudocode, return values and variables

"""
This is multiline comment 
in python
"""
# Ask user for their name
name = input("What's your name? ")

#  Say hello to user

# print("hello, " + name)
# print("hello,", name)
# print("hello,", end = " ")
# print(name)

# print("hello,", name, sep = " what ")

# positional parameters

# named parameters
# print("hello, "friend"")
# print('hello, "friend"')

# \ escape charater
# print("hello, \"friend\"")

# special string
# print(f"hello, {name}")


# Remove whitespace from str
# name = name.strip()


# Capitalize user's name

# name = name.capitalize()
# name = name.title()

# Remove whitespace from str and capitalize user's name
name = name.strip().title()

print(f"hello, {name}")


# arguments , "hello, world"(input) is a argument for print function
