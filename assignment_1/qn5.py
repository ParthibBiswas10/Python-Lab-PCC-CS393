'''5. Find the grade of a student based on five different subjects and the gradation table is given
below:
Average Mark Grade
91-100 O
81-90 A+
71-80 A
61-70 B
51-60 C
41-50 D
33-40 E
Less than 33 F'''
marks=[]
print("Enter marks for 5 subjects:")
for i in range(5):
    mark = int(input(f"Subject {i + 1}: "))
    marks.append(mark)

#for mark in marks:
  #total=total+mark
total=sum(marks)
avg=total/len(marks)
print(f"Avg Mark: {avg:.2f}")
if(avg<33):
    print("fail")
elif(avg>=33 and avg<=40):
    print("Grade: E")
elif(avg>40 and avg<=50):
    print("Grade: D")
elif(avg>=50 and avg<=60):
    print("Grade: C")
elif(avg>60 and avg<=70):
    print("Grade: B")
elif(avg>70 and avg<=80):
    print("Grade: A")
elif(avg>80 and avg<=90):
    print("Grade: A+")
elif(avg>90 and avg<=100):
    print("Grade: O")
    