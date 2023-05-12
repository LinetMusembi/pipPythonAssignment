# Write a function that takes an unknown number of arguments and returns their sum.
def list_items(*nums):
    sum = 0
    for num in nums:
        sum += num
    return sum

nums = list_items(2,3,4,5)
print(nums)


# Write a function that takes two arguments, the first being a string and the second being an unknown 
# number of integers. The function should return a new string where the integers have been added to the 
# original string.

def adding_int(string,*args):
    result = string
    for num in args:
        result += str(num)
    return result    


original_string = "The answer is" " "
new_string = adding_int(original_string,34,56,78,9)
print(new_string)

# Write a function that takes an unknown number of keyword arguments and returns a dictionary where the 
# keys are the argument names and the values are the argument values.

def my_interest(**kwargs):
    return kwargs

result = my_interest(name="Lynet", age=19, email="musembi@gmail.com")
print(result)

# Write a function that takes a function and an unknown number of arguments, and returns the result of 
# calling the function with the arguments.
def call_name(fun, *args):
    return fun(*args)

def many_numbers(a,b):
    return a + b
result = call_name(many_numbers,5,8)
print(result)

# Write a function that takes a list of integers and an unknown number of keyword arguments. 
# The function should return a new list where each integer in the original list has been multiplied by 
# the value of the corresponding keyword argument.
