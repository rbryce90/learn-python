name = "bryce"
age = 29

# concatnate
# print('Hello, my name is ' + name + ' and I am ' + str(age))


# arguments by position
# print("My name is {name} and I am {age}".format(name=name, age=age))


# f-strings
# print(f'Hello, my name is {name} and I am {age}')


# string methods
s = 'hello world'

# string methods
print("started with", s)

print("capitalize", s.capitalize())

print("upper", s.upper())

print("lower", s.lower())

print("swapcase", s.swapcase())

print("replace", s.replace('world', 'everyone'))

sub = 'h'

print("count --> how many of a letter", sub.count(sub))

print("startswith returns bullion, for weather it starts with paramater ===>",
      s.startswith("hello"))

print("endswith, boolean if it ends with paramater ===>", s.endswith('d'))

print("split, turns all words into a list", s.split())

print("find, finds index of character", s.find('r'))


# check to see if types of characters are particular type
print("isalpha, false because of space", s.isalpha())
print("isalnum", s.isalnum())
print("isalnumeric", s.isnumeric())
