import random

# Line 1: Random integer between 5 and 20 (both inclusive)
print(random.randint(5, 20))  # line 1
# What did you see on line 1?
# Answer: I saw a random integer between 5 and 20.
# What was the smallest number you could have seen, what was the largest?
# Answer: The smallest number is 5, the largest number is 20.

# Line 2: Random number from the range 3 to 10 with a step of 2 (3, 5, 7, 9)
print(random.randrange(3, 10, 2))  # line 2
# What did you see on line 2?
# Answer: I saw one of the numbers: 3, 5, 7, or 9.
# What was the smallest number you could have seen, what was the largest?
# Answer: The smallest number is 3, the largest number is 9.
# Could line 2 have produced a 4?
# Answer: No, it could not produce a 4 because the step is 2 and 4 is not part of the sequence.

# Line 3: Random floating-point number between 2.5 and 5.5
print(random.uniform(2.5, 5.5))  # line 3
# What did you see on line 3?
# Answer: I saw a random floating-point number between 2.5 and 5.5.
# What was the smallest number you could have seen, what was the largest?
# Answer: The smallest number is 2.5, the largest number is 5.5.

# Random number between 1 and 100 inclusive
random_number = random.randint(1, 100)
print(random_number)
