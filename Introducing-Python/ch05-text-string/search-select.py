poem = '''All that doth flow we cannot liquid name
Or else would fire and water be the same;
But that is liquid which is moist and wet
Fire that property can never get.
Then 'tis not cold that doth the fire put out
But 'tis the wet that makes it die, no doubt.'''

print(poem[:13])
print(len(poem))

print(poem.startswith('All'))

print(poem.endswith('That\'s all, folks!'))

word = 'the'
print(poem.rfind(word))
print(poem.rindex(word))

# word = 'duck'
# print(poem.rfind(word))
# print(poem.rindex(word))

word = 'the'
print(poem.count(word))

print(poem.isalnum())

# case

setup = 'a duck goes into a bar...'
print(setup.strip('.'))

print(setup.capitalize())
print(setup.upper())
print(setup.lower())
print(setup.swapcase())

# alignment

print(setup.ljust(30))
print(setup.rjust(30))
