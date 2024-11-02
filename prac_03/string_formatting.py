"""
f-string formatting to get the output
"""
name = "Gibson L-5 CES"
year = 1922
cost = 16035.9
print(f"{year} {name} for about ${cost.__round__():,}!")


"""
Using a for loop with the range function to test the f-string formatting
"""
for i in range(0,11,1):
    number = 2 ** i
    print(f"2 ^ {i:>2} is {number:>4}")
