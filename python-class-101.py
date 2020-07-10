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
# Other useful built-in methods are split and join. Split returns substrings separated by delimiters (or whitespaces if undefined):
str5 = "aaa-bbb-ccc"
print(str5)
str5subs = str5.split("-")
print(str5subs)
# Join does just the opposite, but with the iterable (list, tuple, string, etc.) inside the parentheses and the delimiter outside:
str5join = ", ".join(str5subs)
print(str5join)
print()
# Slicing & dicing: Python also offers a more practical way to divide and work with segments of lists and strings with the s[*start*:*end*] (exclusive) slice (remember that the index is zero-based):
str6 = "Python"
print(str6)
print(str6[1:4])
print(str6[1:])
print(str6[:4])
print()
# Pay special attention to the s[:] case. This is the Pythonic way to make a copy of a sequence:
print(str6[:])
print()
# Python also uses negative numbers to offer easy access to the end of a string (inclusive in this case), counting back from -1:
print(str6[-1])
print(str6[:-3])
print(str6[-3:])
print()
# Combining the two indexes, we can conclude that for any index *n*, s[:n] + s[n:] == s, always dividing the sequence in two parts and conserving all characters.
# We can also combine them to quickly reverse the sequence or parts of it:
print(str6[::-1])
print(str6[1::-1]) # First two items, reversed.
print(str6[:-3:-1]) # Last two items, reversed.
print(str6[-3::-1]) # Everything except the last two items, reversed.
print()
# There's a built-in list class, written with [] square brackets.
# You can use the len() function with lists, just as with strings, and elements follow zero-based numbering.
colors = ["green", "blue", "yellow"]
print(colors)
print(colors[0])
print(colors[2])
print(len(colors))
print()
# Construct *for* can quickly look at each element in a list in turn:
sequence = [1, 2, 3, 4, 5]
print(sequence)
total = 0
for i in sequence:
    total = total + i
print(total)
print()
# Using *in* is an easy way to test if an element appears in the list:
brothers = ["Chico", "Harpo", "Groucho"]
print(brothers)
if "Harpo" in brothers:
    print("Yay!")
print()
# CONTINUE WITH TUPLES (PAGE 67)
print()
# And finally, a neat Easter egg to inspire your journey:
import this

