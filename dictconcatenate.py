

# merging of dictionaries using built in function


dict1={1:10, 2:20}
print(dict1)


dict2={3:30, 4:40}
print(dict2)


dict3={5:50,6:60}
print(dict3)

dict1.update(dict2)
print("concatenated dict is:" )
print(dict1)

dict1.update(dict3)
print("final concatenate dict is:")
print(dict1)



