describe = '''
Besides the functions in the previous section, Python has three ways of \
formatting strings:
old style (supported in Python 2 and 3) = % ()
new style (Python 2.6 and up) = {} and format()
f-strings (Python 3.6 and up) = f""
'''
print(describe)

# old style
old_style = '''
%s\t\t string
%d\t\t decimal integer
%x\t\t hex integer
%o\t\t octal integer
%f\t\t decimal float
%e\t\t exponential float
%g\t\t decimal or exponential float
%%\t\t a literal %
'''
print(old_style)

print('\nexample: ')
print('integer: ')
print('%s' % 42)
print('%d' % 42)
print('%x' % 42)
print('%o' % 42)

print('\nfloat: ')
print('%s' % 7.03)
print('%f' % 7.03)
print('%e' % 7.03)
print('%g' % 7.03)

print('\nan integer and literal with %%')
print('%d%%' % 100)

# string and integer interpolation
actor = 'Richard Gere'
cat = 'Chester'
weight = 28

print('My wife\'s favorite actor is %s' % actor)
print('Our cat %s weight %s pounds' % (cat, weight))

# padding
print('\npadding a string: \n')
thing = 'woodchuck'
print('%s' % thing)
print('%12s' % thing)
print(len('%s' % thing))
print(len('%+12s' % thing))
print(len('%-12s' % thing))

print('%0.3s' % thing)
print('%12.3s' % thing)
print('%-12.3s' % thing)

print('\npadding an integer: \n')
thing = 9876
print('%d' % thing)
print('%12d' % thing)
print('%-12d' % thing)
print('%.3d' % thing)
print('%-.3d' % thing)
print('%12.d' % thing)
print('%-12.3d' % thing)

print('\npadding a float: \n')
thing = 98.6
print('%f' % thing)
print('%12f' % thing)
print('%+12f' % thing)
print('%-12f' % thing)
print('%12.3f' % thing)
print('%-12.3f' % thing)

print('\nnew style format with " {} ": ')

thing = 'woodchuck'
place = 'lake'
print('The {} is in the {}.'.format(thing, place))

print('The {1} is in the {0}'.format(thing, place))

print('The {thing} is in the {place}.'.format(thing='duck', place='bathup'))

# dictionary
print('\ndictionary: ')
d = {'thing': 'duck', 'place': 'bathup'}
print('The {0[thing]} is in the {0[place]}.'.format(d))


thing = 'wraith'
place = 'window'
print('The {} is at the {}'.format(thing, place))
print('The {:12s} is at the {:12s}'.format(thing, place))
print('The {:<12s} is at the {:<12s}'.format(thing, place))
print('The {:^12s} is at the {:^12s}'.format(thing, place))
print('The {:>12s} is at the {:>12s}'.format(thing, place))
print('The {:!^12s} is at the {:!^12s}'.format(thing, place))

print('\nnewest style with f"{}":')

new_style = '''with new style we have alot of power'''
print(new_style)

thing = 'wereduck'
place = 'werepond'
print(f'The {thing.capitalize()} is in the {place.upper()}')

print(f'The {thing:>20} is in the {place.upper():.^20}')

# only valid in python 3.8
# print(f'{thing =}, {place =}')

# examp:

email_template = '''
Dear {salutation} {name},

Thank you for your letter. We are sorry that our {product}
{verbed} in your {room}. Please note that it should never
be used in a {room}, especially near any {animals}.

Send us your receipt and {amount} for shipping and handling.
We will send you another {product} that, in our tests,
is {percent}% less likely to have {verbed}.

Thank you for your support.

Sincerely,
{spokesman}
{job_title}
'''

salutation = 'Awesome'
name = 'Rambo'
product = 'Flying machine'
verbed = 'falling of'
room = 'bath room'
animals = 'dog'
amount = '10'
percent = '70'
spokesman = 'Silvestre'
job_title = 'Senior Marketing'

print(email_template % (salutation, name, product, verbed, room, room,
                        animals, amount, product, percent, verbed,
                        spokesman, job_title))
