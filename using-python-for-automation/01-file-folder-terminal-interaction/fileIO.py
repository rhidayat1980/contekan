f = open('inputFile.txt', 'r')
print(f.read())
f.close()

print()

# with context
with open('inputFile.txt') as file:
    f = file.read()
print(f)


# # filter only passed person

passFile = open('passFile.txt', 'w')
f = open('inputFile.txt', 'r')

for line in f:
    line_split = line.split()
    if line_split[2] == 'P':
        passFile.write(line)
f.close()
passFile.close()


# # filter only failed person
failedFile = open('failedFile.txt', 'w')
f = open('inputFile.txt', 'r')

for line in f:
    line_split = line.split()
    if line_split[2] == 'F':
        failedFile.write(line)
f.close()
failedFile.close()


# # or combined them together
f = open('inputFile.txt', 'r')
passFile = open('passFile.txt', 'w')
failedFile = open('failedFile.txt', 'w')

for line in f:
    line_split = line.split()
    if line_split[2] == 'P':
        passFile.write(line)
    else:
        failedFile.write(line)

f.close()
passFile.close()
failedFile.close()
