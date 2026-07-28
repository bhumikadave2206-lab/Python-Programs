# (24) Dictionary Functions/Methods Example   
d = {'name': 'bhumika', 'age': 19, 'city': 'jamnagar'}

print("Original dictionary:", d)
print("Length:", len(d))
print("Get Your Age:", d.get('age'))
d.update({'gender': 'FeMale'})
print("After updation d is :", d)
d.pop('city')
print("After Your City Is :", d)
d['country'] = 'India'
print("After adding key Your Counrty iss ", d)
print(" Your Keys are these:", d.keys())
print("Your Keys are these Values:", d.values())
print("Items:", d.items())
d2 = d.copy()
print("Copied dictionary is these:", d2)
d.clear()
print("After clear:", d)