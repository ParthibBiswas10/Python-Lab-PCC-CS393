'''6.Merge following two Python dictionaries into one dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}'''

dict1={
    'ten':10,
    'tw':20,
    'th':30
}
dict2={
    'th':30,
    'for':40,
    'fif':50
}
dict1.update(dict2)
print(dict1)