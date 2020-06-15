one = 'Snap'
two = 'crackle'

print(type(one))
print(type(two))

print(one, two)

# string with '' or "" or """ """ or ''' '''

single_quoted = 'Hello Python!'
double_quoted = "Hello again, Python!"
triple_quoted = """Hello again, Python!"""
triple_single_quoted = '''Hello again, Python!'''

print(single_quoted)
print(double_quoted)
print(triple_quoted)
print(triple_single_quoted)


poem = '''\nI do not like thee, Doctor Fell.
\tThe reason why, I cannot tell.
\t\tBut this I know, and know full well:
\t\t\tI do not like thee, Doctor Fell.
 '''

print(poem)

greeting = """'Guten Morgen, mein Herr!'
\n\tsaid mad king Ludwig to his wig."""

print(greeting)

# create a string with str()
print()
print(str(98.0))
print(str(1.0e4))
print(str(True))
print(str([1, 2, 3, 4]))
print(str(set(range(1, 10))))
print(str(tuple(range(1, 10))))


# escape with \
palindrome = 'A man,\nA plan,\nA canal:\nPanama.'
print(palindrome)

print('\tabc')
print('a\tbc')
print('ab\tc')
print('abc\t')
