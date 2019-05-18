# x = 1 int
# y = 2.5 float
# name = 'bryce'
# is_cool = True

# print("x =", x, "y =", y)


# multiple varibles
x, y, name, is_cool = (1, 2.5, 'Bryce', True)


print(x, y, name, is_cool)

print(1 + 2)

# casting
x = str(x)

# changes to integer from float, which changes it to a 2
y = int(y)

# changes back to float, which allows decimal but will remain 2, the point something is no longer there
y = float(y)


print(type(x))

print(type(y), y)
