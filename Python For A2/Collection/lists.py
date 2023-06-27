
# Collection = single "variable" used to store multiple values
# List = [] ordered and changeable. Duplicates OK
# Set = {} unordered and immutable, but add/remove OK. NO duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER

fruits = ["apple", "banana", "pineapple", "mango"]
drinks = ["coke", "spite", "sting", "fanta"]

# if we used index by -1 it will go to the last value
# print(fruits[-1])
# print(fruits[0:3])

# Modifying
# fruits.append("Panda")
# fruits.pop()
result = fruits.pop(1)
print(result)
print(fruits)

# print(fruits.__dir__())
# print('art' in fruits)
# for item in fruits:
#     print(item)



