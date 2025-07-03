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
# re.match(pattern, string, flags=0)               # used to check if the beginning of a string matches a pattern
# re.search(pattern, string, flags=0)              # used to search for the first occurrence of a pattern in a string
# re.findall(pattern, string, flags=0)             # used to find all occurrences of a pattern in a string
# re.finditer(pattern, string, flags=0)            # used to find all occurrences of a pattern in a string and return an iterator yielding match objects
# re.sub(pattern, repl, string, count=0, flags=0)  # used for replacing occurrences of a pattern in a string
# re.split(pattern, string, maxsplit=0, flags=0)   # used to split a string by the occurrences of a pattern

# NOT IMPORTANT:
# re.escape(string)                                # used to escape all non-alphanumeric characters in a string
# re.compile(pattern, flags=0)                     # used to compile a regular expression pattern into a regex object
# re.subn(pattern, repl, string, count=0, flags=0) # used to replace occurrences of a pattern in a string and return a tuple containing the new string and the number of replacements made
# re.fullmatch(pattern, string, flags=0)           # used to check if the entire string matches a pattern
# re.purge()                                       # used to clear the cache of compiled regular expressions
# re.setstarter()                                  # used to set the starting point for the next search operation
# re.DEBUG                                         # used to enable debugging output for regular expression operations


# text="Contact us at 123-456-7890 or 987-654-3210 for more information."
# import re
# digits = re.findall(r'\d+', text)
# print("Digits found in the text:", digits)

# import re 
# def clean_text(text):
#     # Remove special characters and digits
#     cleaned_text = re.sub(r'[^a-zA-Z\w\s]', '', text)
#     # Remove extra spaces
#     cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
#     return cleaned_text

# # Example usage
# text = "Hello, World! 1234 This is a test text with special characters & symbols."
# cleaned_text = clean_text(text)
# print("Original Text:", text)
# print("Cleaned Text :", cleaned_text)

# def is_palindrome(s):
#     text = " ".join(char.lower() for char in s if char.isalnum())  # Normalize the string by removing non-alphanumeric characters and converting to lowercase
#     print(text)
#     print(text[::-1])
#     return text == text[::-1]  # Check if the string is equal to its reverse


# # Example usage
# input_string = input("Enter a string: ")
# if is_palindrome(input_string):
#     print(f'"{input_string}" is a palindrome.')
# else:
#     print(f'"{input_string}" is not a palindrome.')

# # write a program to count the number of vowels in a string
# def count_vowels(s):
#     vowels = "aeiouAEIOU"
#     count = 0
#     for char in s:
#         if char in vowels:
#             count += 1
#     return count
# # Example usage
# input_string = input("Enter a string: ")
# vowel_count = count_vowels(input_string)
# print(f"The number of vowels in the string is: {vowel_count}")

#write a program to find and replace all email addresses in a text using regular expressions
# import re
# def replace_emails(text, replacement):
#     email_pattern = r'[a-zA-Z0-9._%+-]+@gmail+\.[a-zA-Z]{2,}' # Regular expression pattern to match email addresses
#     modified_text = re.sub(email_pattern, replacement, text)          # Replace all email addresses with the replacement string
#     return modified_text
# # Example usage
# text = "Please contact us at john.doe@gmail.com or jane.doe@gmail.com for more information."
# replacement = "[REDACTED]"
# modified_text = replace_emails(text, replacement)
# print("Original Text:", text)
# print("Modified Text:", modified_text)

#write a program to reverse the words in a string while preserving the order of the words
# def reverse_words(s):
#     words = s.split()  # Split the string into words
#     reversed_words = ' '.join(reversed(words))  # Reverse the order of words and join them back into a string
#     return reversed_words
# # Example usage
# input_string = input("Enter a string: ")
# reversed_string = reverse_words(input_string)
# print("Reversed Words:", reversed_string)

#FILE HANDLING
# functions in file handling:
# 1. open() - opens a file in read or write mode
# 2. close() - closes the file
# 3. read() - reads the content of the file
# 4. write() - writes content to the file
# 5. readline() - reads a single line from the file
# 6. readlines() - reads all lines from the file and returns a list
# 7. seek() - moves the file pointer to a specific position in the file
# 8. tell() - returns the current position of the file pointer in the file
# 9. flush() - flushes the internal buffer of the file

# with open('example.txt', 'w') as file:
#     file.write('Hello, World!\n')  
#     file.writelines(["This is line 1\n","This is Line 2\n"])

# with open('example.txt','r') as file:
#     for line in file:
#         print(line.strip())
#         print(file.readline())

# Function to count the number of words and lines in a file
# def count_words_and_lines(filename):
#     try:
#         with open(filename,'r') as file:
#             lines = file.readlines()
#             line_count = len(lines)
#             word_count = sum(len(line.split()) for line in lines)
            
#             print(f"Number of lines: {line_count}")
#             print(f"Number of words: {word_count}")
#     except FileNotFoundError:
#         print(f"The file '{filename}' does not exist.")

# count_words_and_lines('example.txt')

# Function to write a list of items to a file and read them back
# This function writes a list of items to a file, each on a new line, and reads them back to display the contents of the file.
# def write_item_to_file(filename,items):
#     try:
#         with open(filename,'w') as file:
#             for item in items:
#                 file.write(f"{item}\n")
#     except Exception as e:
#         print(f"An error occurred while writing to the file: {e}")
        
# def read_items_from_file(filename):
#     try:
#         with open(filename,'r') as file:
#             items = file.readlines()
#             print("Items in the file:")
#             for item in items:
#                 print(item.strip())
#     except FileNotFoundError:
#         print(f"The file '{filename}' does not exist.")

# fruits=["Apple", "Banana", "Cherry", "Date"]

# write_item_to_file('fruits.txt', fruits)
# read_items_from_file('fruits.txt')

# Program to copy the contents of one file to another
# def copy_file_contents(source_file, destination_file):
#     try:
#         with open(source_file, 'r') as source, open(destination_file, 'w') as destination:
#             content = source.read()
#             destination.write(content)
#             print(f"Contents copied from '{source_file}' to '{destination_file}'.")
#     except FileNotFoundError:
#         print(f"The file '{source_file}' does not exist.")
#     except Exception as e:
#         print(f"An error occurred: {e}")
# source_file = 'example.txt'
# destination_file = 'copied_example.txt'
# copy_file_contents(source_file, destination_file)

# Program that counts the number of occurrences of a specific word in a text file
# def count_word_occurrences(filename, word):
#     try:
#         with open(filename, 'r') as file:
#             content = file.read()
#             word_count = content.lower().split().count(word.lower())
#             print(f"The word '{word}' occurs {word_count} times in the file '{filename}'.")
#     except FileNotFoundError:
#         print(f"The file '{filename}' does not exist.")
#     except Exception as e:
#         print(f"An error occurred: {e}")
# filename = 'example.txt'
# word_to_count = input("Enter the word to count occurrences: ")
# count_word_occurrences(filename, word_to_count)

