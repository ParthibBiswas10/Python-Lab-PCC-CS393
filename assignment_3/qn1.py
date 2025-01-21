'''1. Reduce a string of lowercase characters in range ascii [a..z] by doing a series of
operations. In each operation, select a pair of adjacent letters that match, and delete them.
Delete as many characters as possible using this method and return the resulting string. If the
final string is empty, return Empty String.
a. Input- aaabccddd, output- abd, input- abba output-empty string.'''

str=input("Input String: ")
stack=[]
for char in str:
    if stack and stack[-1]==char:
        stack.pop()
    else:
        stack.append(char)
if stack:
    s="".join(stack)
    print(s)
else:
    print("Empty String")