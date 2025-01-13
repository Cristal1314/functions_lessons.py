# *agrs = allows you to pass multiple non-key argumrents
#  **Kwargs = allows you to pass multiple keyqwords-arguments 
#           *unpacking opertator
#         1. positional 2. defualt  3. keywords 4. ARBITRAY 


# def add(*nums):
#     # print(type(agrs))
#     total = 0
#     for num in nums:
#         total += arg
#         return total
    
#     print(add(1))

#-----------------------------------------------------------------

# def display_name(*args):
#     for arg in args:
#         print(arg, end="")

# display_name("Dr.", "Spongbob ", "Harold ", "Squarpants ")

#----------------------------------------------------------------

def print_address(**kwargs):
   for key, value in kwargs.items():
      print(f"{key}: {value}")


print_address(Street=" 6042 s Komensky ",
               City= "Chicago ",
               State="Illinos", 
               Zipcode= "60629" ,)


# Indefinite Arguments (*args) Practice #1
# Create a function called sum_squares that takes any number of numeric arguments, and returns the sum of their values squared.

# For example for the arguments sum_squares(1,2,3) it should return 14 (1+4+9).


# Indefinite Arguments (*args) Practice #2
# Create a function called absolute_sum, which takes any number of arguments, and returns the sum of their absolute values (that is, it takes the non-negative values and adds them together, in other words, considers them all - negative and positive - as positive).

# Indefinite Arguments (*args) Practice #3
# Create a function called personal_numbers that receives, as its first argument, a name, and then an indefinite number of values.

# The function should return the following message:

# "{name}, the sum of your numbers is {sum_numbers}"