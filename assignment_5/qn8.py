'''7. Check if a value 200 exists in a dictionary sampleDict = {'a': 100, 'b': 200, 'c': 300}'''

sampleDict = {'a': 100, 'b': 200, 'c': 300}
n=int(input("Enter Number: "))
if n in sampleDict.values():
    print("Found")

else:
    print("Not found")
#print(list(sampleDict.values()))