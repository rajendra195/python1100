import random

print("Welcome to the number guessing game!!")

num = random.randint(1, 100)
print(num)

user_num = int(input("Guess a number between 1 to 99: "))

class Guess:
    def __init__(self, num, user_num):
        self.num = num
        self.user_num = user_num

    def guess_number(self):
        if self.num > self.user_num:
            print("greater")
        elif self.num < self.user_num:
            print("less")
        elif self.num == self.user_num:
            print("You got it!! You guessed the right number.")

a = Guess(num=num, user_num=user_num)
a.guess_number()