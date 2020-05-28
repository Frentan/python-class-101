# Starting out with a simple addition program:
num1 = 2
num2 = 1
sum = num1 + num2
print(sum)
# Use *print()* to insert empty lines and keep your output orderly:
print()
# Unlike JavaScript and C, it's not mandatory to use semicolons at the end of statements.
# Neither are {} curly brackets used to represent blocks. Everything is done with indentation:
"""
I_am_a_parent
    I_am_a_child
        I_am_a_grandchild
    I_am_another_child
        I_am_another_grandchild
"""
# Variables "store" values. To use the classic example:
message = "Hello, World!"
print(message)
# But we can change a variable's value at any point:
message = "Python is my favorite programming language :-)"
print(message)
# Variable names can only have letters, numbers, and underscores, but they cannot start with a number or be the same as reserved keywords.
print()
# Python has a built-in string class. They are bound by either single or double quotation marks.
# Strings in Python are immutable, or unchangeable, once created (just like in Java).
# String characters can be accessed using standard [] square bracket syntax and zero-based numbering.
str1 = "hi"
print(str1[0])
print(str1[1])
print(len(str1))
print(str1 + " there")
print()
# However, unlike in Java, the + operator does not change numbers or other data types to strings. It's necessary to use the *str()* function instead:
pi = 3.141592
str2 = "The value of pi is " + str(pi)
print(str2)
print()
# You can easily make the whole string upper or lower case with their respective methods:
str3 = "eXaMpLe"
print(str3)
print(str3.upper())
print(str3.lower())
print()
# It's also easy to strip a string of leading or trailing whitespaces (by default) or any other characters defined in the parameters:
str4 = "   a...foo,,,b   "
print(str4)
str4 = str4.strip()
print(str4)
str4 = str4.strip("a.,b")
print(str4)
print()
# CONTINUE WITH SPLIT METHOD (PAGE 62)
print()
# And finally, a neat Easter egg to inspire your journey:
import this

