# Let's learn about LOOPS in Python!

# --------------------------------
# 1. FOR LOOP: Repeats a block of code a certain number of times
# --------------------------------

print("Counting from 1 to 5 with a for loop:")
for i in range(1, 6):  # range(start, stop) goes from 1 to 5
    print("Number:", i)


# --------------------------------
# 2. FOR LOOP with a LIST
# --------------------------------

fruits = ["apple", "banana", "cherry"]
print("\nLet's print each fruit in the basket:")

for fruit in fruits:
    print("I like", fruit)


# --------------------------------
# 3. WHILE LOOP: Repeats *while* a condition is True
# --------------------------------

print("\nCounting up to 5 with a while loop:")
count = 1
while count <= 5:
    print("Count is:", count)
    count += 1


# --------------------------------
# 4. WHILE LOOP with a condition and break
# --------------------------------

print("\nRolling a dice until we get a 6:")

import random
roll = 0

while roll != 6:
    roll = random.randint(1, 6)
    print("Rolled:", roll)

print("🎉 Got a 6! Loop ended.")


# --------------------------------
# 5. Loop with IF condition inside
# --------------------------------

print("\nEven or Odd from 1 to 10:")

for num in range(1, 11):
    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")
