quotes = {
    "Moe": "A wise guy, huh?",
    "Larry": "Ow!",
    "Curly": "Nyuk nyuk!",
}

stooge = "Curly"
print(stooge, "says:", quotes[stooge])

for key, value in quotes.items():
    print(key, "=", value)
