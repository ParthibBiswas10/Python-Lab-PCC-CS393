'''Say a box of cookies can hold 24 cookies, and a container can hold 75 boxes of cookies.
Write a program that prompts the user to enter the total number of cookies, then outputs the
number of boxes and the number of containers to ship the cookies. Note that each box must
contain the specified number of cookies, and each container must contain the specified number
of boxes. If the last box of cookies contains less than the number of specified cookies, you can
discard it and output the number of leftover cookies. Similarly, if the last container contains less
than the number of specified boxes, you can discard it and output the number of leftover boxes.'''

max_cook= 24
max_box=75
cookies=int(input("koto gulo cookies? "))
total_box=cookies//max_cook
if cookies>0 and cookies<=24:
    print("requied number of box: 1 & cookies left: 0")

else:
    print(f"required number of boxes: {total_box} & cookies left: {cookies%max_cook}")
if(total_box>=max_box):
    cont=total_box//max_box
    print(f"total container required: {cont} & box left: {total_box%max_box}")
elif (total_box>0 and total_box<=75): 
    print("1 container required")


