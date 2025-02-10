phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)

if "Jack" in phonebook:  
    print("Jake is listed in the phonebook.")

phonebookb = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(phonebookb)

for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

del phonebook["John"]
phonebook.pop("Jack") # idem previous
print(phonebook)


