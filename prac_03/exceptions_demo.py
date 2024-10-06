"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
Ans: It will occur when the numerator and denominator are not integers.
2. When will a ZeroDivisionError occur?
Ans: It will occur when denominator is input as zero.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Ans: We can validate in the input not taking as 0. We can run a condition if the value is entered zero, it again asks
for the value.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")