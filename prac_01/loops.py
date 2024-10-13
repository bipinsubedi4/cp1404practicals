for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c
stars = int(input("Number of stars: "))
for i in range(0, stars, 1):
    print("*", end='')
print()

# d
stars = int(input("Number of stars: "))
for i in range(0, stars, 1):
    for j in range(0, i+1, 1):
        print("*", end='')
    print()
