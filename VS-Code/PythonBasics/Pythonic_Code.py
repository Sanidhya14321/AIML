# List Comprehensions
# These provide a concise way to create lists in Python in a single line of code.
# Example 1: Create a list of squares of even numbers from 0 to 9
# squares = [x**2 for x in range(100) if x % 2 == 0]
# print(squares)  

# Lambda Functions
# These are small anonymous functions defined with the lambda keyword.

# add= lambda x, y: x + y
# print(add(5, 3))  # Output: 8
# Example 2: Sort a list of tuples by the second element
# data = [(1, 'apple'), (3, 'banana'), (2, 'cherry')]
# sorted_data = sorted(data, key=lambda x: x[1])
# print(sorted_data)  # Output: [(2, 'cherry'), (1, 'apple'), (3, 'banana')]

# map() function applies a function to all items in an input list (or any iterable).
# list1=[1,2,3,4,5]
# squares=map(lambda x:x**2,list1)
# print(list(squares))  # Output: [1, 4, 9, 16, 25]

# filter() function filters items out of an iterable based on a function that returns True or False.
# list2 = [1, 2, 3, 4, 5]
# evens = filter( lambda x : x % 2 == 0 , list2)
# print(list(evens))  # Output: [2, 4]

# reduce() function reduces an iterable to a single value by applying a function cumulatively.
# from functools import reduce
# numbers = [1, 2, 3, 4, 5]
# product = reduce(lambda x, y:x * y, numbers)
# print(product)  # Output: 120

# #decorators
# # Decorators are a way to modify or enhance functions or methods without changing their code.
# # They are a powerful tool for functional programming in Python.
# # Example 1: A simple decorator that prints a message before and after a function call
# def decorator_function(original_function):
#     def wrapper_function(*args, **kwargs):
#         print("Before the function call")
#         result = original_function(*args, **kwargs)
#         print("After the function call")
#         return result
#     return wrapper_function
# @decorator_function
# def add(a, b):
#     print("Inside the function")
#     return a + b
# print(add(5, 3))  # Output: Inside the function, Before the function call

