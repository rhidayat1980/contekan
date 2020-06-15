import string
world = "    earth     "
print(world.strip())

print(world.strip(' '))

print(world.lstrip())
print(world.rstrip())

# nothing happens
print(world.strip('!'))


blurt = "What the...!!?"
print(blurt.strip('.!?'))


print(string.whitespace)
print(string.punctuation)

print(world.strip(string.whitespace))
print(blurt.strip(string.punctuation))

prospector = "What in tarnation ...??!!"
print(prospector.strip(string.whitespace + string.punctuation))
