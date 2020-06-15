crypto_list = ['Yeti', 'Bigfoot', 'Loch Ness Monster']
crypto_string = ','.join(crypto_list)
print('Found and signing book deals:', crypto_string)


for name in crypto_list:
    print('Found and signing book deals:', name)

for index, value in enumerate(crypto_list):
    print(f"{index}. Found and signing book deals: {value}")
