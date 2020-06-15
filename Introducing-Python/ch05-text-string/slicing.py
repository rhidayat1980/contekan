letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[0])
print(letters[1:10])

print(letters[-1])
print(len(letters))
print(letters[len(letters) - 2])

# string is immutable
name = 'Henny'
print(name.replace('H', 'B'))
print(name)

print('B' + name[1:])
print(letters[-1::-1])


# get length with len()
print(len(letters))

empty = ""
print(len(empty))
