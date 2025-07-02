#CHECK IF A PRIME NUMBER
# num=int(input("Enter a no. :"))

# if num>1:
#     for i in range(2,int(num**0.5)+1):
#         if num%i==0:
#             print(num,"is not a prime no.")
#         else:
#             print(f"{num} is a prime no.")
# else:
#     print(f"{num} is not a prime no.")


# FACTORIAL OF A NUMBER
# num = int(input("Enter a number:"))

# def factorial(a):
#     if a == 0:
#         return 1
#     else:
#         return a * factorial(a - 1)

# print(factorial(num))


#PROGRAM FOR LARGEST NUMBER IN A LIST WITHOUT max() FUNCTION
# def find_largest_number(lst):

#     if not lst:
#         return None  
#     largest_num = lst[0]
#     for num in lst[1:]:
#         if num > largest_num:
#             largest_num = num
#     return largest_num

# numbers = [12, 45, 7, 23, 56, 89, 34]
# print(find_largest_number(numbers))

# list1=[1,2,3,6,7,4,4,6,11]

# reversedlist=[]
# for i in range(len(list1)-1,-1,-1):
#     reversedlist.append(list1[i])

# reversedSet=set(reversedlist)

# print(reversedlist)
# print(reversedSet)

# studentGrades = {}

# c = int(input("Enter number of subjects: "))

# for i in range(c):
#     name = input("Enter name: ")
#     grade = int(input("Enter grade: "))
#     studentGrades[name] = grade

# if studentGrades:
#     avg = sum(studentGrades.values()) / len(studentGrades)
#     studentGrades["avg"] = avg

# for key, value in studentGrades.items():
#     print(f"{key} {value}")

#REGULAR EXPRESSION TO CHECK IF A STRING IS A VALID EMAIL
#Regular expressions, often referred to as regex or regexp, are a powerful tool in Python for pattern matching and manipulating strings
# import re
# def validate_email(email):
#     pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
#     if re.match(pattern, email):
#         return True
#     else:
#         return False
#     # Testing the function
# email = input("Enter an email address: ")
# if validate_email(email):
#     print("Valid email address")
# else:
#     print("Invalid email address")

# ALL FUNCTIONS IN re module
# IMPORTANT:
# import re
# re.match(pattern, string, flags=0) used to check if the beginning of a string matches a pattern
# re.search(pattern, string, flags=0) used to search for the first occurrence of a pattern in a string
# re.findall(pattern, string, flags=0) used to find all occurrences of a pattern in a string
# re.finditer(pattern, string, flags=0) used to find all occurrences of a pattern in a string and return an iterator yielding match objects
# re.sub(pattern, repl, string, count=0, flags=0) used for replacing occurrences of a pattern in a string
# re.split(pattern, string, maxsplit=0, flags=0) used to split a string by the occurrences of a pattern

# NOT IMPORTANT:
# re.escape(string) # used to escape all non-alphanumeric characters in a string
# re.compile(pattern, flags=0) # used to compile a regular expression pattern into a regex object
# re.subn(pattern, repl, string, count=0, flags=0) # used to replace occurrences of a pattern in a string and return a tuple containing the new string and the number of replacements made
# re.fullmatch(pattern, string, flags=0)    # used to check if the entire string matches a pattern
# re.purge() # used to clear the cache of compiled regular expressions
# re.setstarter()   # used to set the starting point for the next search operation
# re.DEBUG # used to enable debugging output for regular expression operations

# text="Contact us at 123-456-7890 or 987-654-3210 for more information."
# import re
# digits = re.findall(r'\d+', text)
# print("Digits found in the text:", digits)
