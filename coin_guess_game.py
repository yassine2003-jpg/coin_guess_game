import random

print("Welcome to the Coin Guessing Game!")
print("Choose a method to toss the coin:")
print("1 - Use random.random()")
print("2 - Use random.randint()")

try:
    method = int(input("Enter 1 or 2: "))
except ValueError:
    print("Invalid input! Please enter a number.")
    exit()

guess = input("Please choose 'head' or 'tail': ").lower()
if guess not in ["head", "tail"]:
    print("Invalid choice! Please type either 'head' or 'tail'.")
    exit()

# Toss the coin
if method == 1:
    PC_result = "head" if random.random() < 0.5 else "tail"
elif method == 2:
    PC_result = "head" if random.randint(0, 1) == 1 else "tail"
else:
    print("Invalid method. Please enter 1 or 2.")
    exit()

# Compare and show result
if guess == PC_result:
    print(f"🎉 Congratulations! You guessed right. The result is {PC_result}.")
else:
    print(f"❌ Sorry, wrong guess. The result was {PC_result}.")
