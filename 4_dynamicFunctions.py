# Dynamic Functions Practice #1
# Create a function (all_positives) that returns True if all the values in a list are positive, and False if at least one of the values is negative. Create a list named numbers with positive and negative values.

# Don't call the function, you just need to define it.
numbers = [1, -2 , 3, -4, 5, -6, 8, -7] #Created a list named numbers
def all_positives():   # define function 

    positive_nums = [ num for num in numbers if num >= 0 ] 
    if (positive_nums):  # This code it to show that if the list given and is positive then it will print True
        print(True)
    else:    # Else is going to be used as a way to show that if the number not positive in the list then will print False
        print(False)

#--------------------------------------------------------------------------------------------------------------------------------------------
# Dynamic Functions Practice #2
# Create a function (sum_less) that adds the numbers of a list as long as they are greater than 0 and less than 1000, and returns the result of said sum. Create a numbers variable, storing a list of numbers so we can test it.

# def sum_less(list2):       # define sum_less 
#  num=( [ 5,3,100] )  #created a variable storing a list to test

#  if num in list2:                         
#   if num in range(0,1000):            
#        num> 0 and num<1000    #checks to see if numbers are greater tha
#  then: 
#    result=num+= 0

# print (result)   #prints the sum of the numbers added all together


       


#--------------------------------------------------------------------------------------------------------------
# Dynamic Functions Practice #3
# Create a function (count_even) that counts the number of even numbers that exist in a list (numbers), and returns the result of said count.
       
# def count_even(list3):  # defines the way that will count_even 
#     numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 ] #This list was created to be able to store in the numnbers
#     even_nums = [ num for num in numbers if num % 2 == 0] # This will be able to generate the even numbers and print them out
#     print(even_nums)
