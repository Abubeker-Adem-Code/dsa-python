# Lists are built-in data structures in python
characters = ['a', 'b', 'c']  # a list of characters
matrix = [[1, 2], [0, -5]]  # a list of lists
zeros = [0] * 3  # using an asterisk we can repeat the item in the list
print(zeros)
# we can concatenate multiple lists using +
# In python every object in a list can be of d/nt type

combined = characters + zeros
print(combined)
print(list(range(1, 19, 2)))
# we can pass any iterable like range() to a list() and convert it to a list
chars = list("Hello word")
print(chars)
numbers = list(range(19))
print(numbers[::-1])

# List unpacking: assigns individual elements of a list to d/nt variables
numbers = [1, 2, 3, 4, 5]
first, second, *other = numbers
# unpacks the first and second item from the list and packs the rest items in to a separate list
print(first, second)
print(other)
letters = ["a", "b", "c"]

for index, letter in enumerate(letters):
    print(index, letter)

# Adding items to a list
letters = ["a", "b", "c"]
letters.append("d")  # append(): adds element at the end of a list

letters.insert(0, "x")  # adds item in a specific position
print(letters)

# removing items from a list
letters.pop()  # removes the item at the end of a list
letters.pop(0)  # removes one item at a given index
letters.remove("c")  # removes the first occurence of letter 'c'
del letters[0:1]  # deletes a range of items
letters.clear()  # removes all the objects in a list
print(letters)

fruits = ["apple", "microsoft", "orange"]
print(fruits.index("microsoft"))  # finds index of an object in a list
# returns the number of occurences of a given item in a list
print(fruits.count("apple"))

numbers = [6, 5, 0]
numbers.sort(reverse=True)
print(numbers)
