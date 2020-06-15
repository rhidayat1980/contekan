disaster = True

if disaster:
    print("Woe!")
else:
    print("Whee!")


# two level if else

furry = False
large = False

if furry:
    if large:
        print("It's yeti.")
    else:
        print("It's a whale!")
else:
    if large:
        print("It's a whale!")
    else:
        print("It's a human. Or a hairless cat.")


color = "mauve"
if color == "red":
    print("It's a tomato")
elif color == "green":
    print("It's a green pepper.")
elif color == "bee purple":
    print("I don't know what it is, but only bees can see it.")
else:
    print("I've never heard of the color.", color)

print(5 == 10)
print(5 < 10)
print(5 > 10)
print(5 != 10)

x = 7
print(5 < x and x > 10)


some_list = []
if some_list:
    print("There's something in here.")
else:
    print("Hey, it's empty.")


letter = "o"

if letter == "a" or letter == "e" or letter == "i" or \
        letter == "o" or letter == "u":
    print(letter, "is vowel")
else:
    print(letter, "is not a vowel")

if letter in "aiueo":
    print(letter, "is vowel")
else:
    print(letter, "is not a vowel")


letter = "o"
vowel_set = {'a', 'i', 'u', 'e', 'o'}
if letter in vowel_set:
    print(letter, "is vowel")
else:
    print(letter, "is not a vowel")


letter = "o"
vowel_list = ['a', 'i', 'u', 'e', 'o']
if letter in vowel_list:
    print(letter, "is vowel")
else:
    print(letter, "is not a vowel")


letter = "o"
vowel_tuple = ('a', 'i', 'u', 'e', 'o')
if letter in vowel_tuple:
    print(letter, "is vowel")
else:
    print(letter, "is not a vowel")


letter = "o"
vowel_dict = {
    'a': 'apple',
    'i': 'impala',
    'u': 'unicorn',
    'e': 'elephant',
    'o': 'ocelot',
}

if letter in vowel_dict:
    print(letter, "is vowel")
else:
    print(letter, "is not a vowel")


letter = 'o'
vowel_string = 'aiueo'
if letter in vowel_string:
    print(letter, "is vowel")
else:
    print(letter, "is not a vowel")


tweet_limit = 280
tweet_string = "Blah" * 60
diff = tweet_limit - len(tweet_string)

if diff >= 0:
    print("a fitting tweet")
else:
    print("went over by", abs(diff))
