'''3. Write programs as per following specifications: ''Print the length of the longest
string in the list of strings str_list. Precondition : the list will contain at least one
element.'''

str_list=[]
size=int(input("Enter Size of List: "))
for i in range(size):
    a=input(f"Enter String {i+1}: ")
    str_list.append(a)
max=0
long=""
for i in str_list:
    if(len(i)>max):
        max=len(i)
        long=i
print(f"max string is: {long} of Size {max}")