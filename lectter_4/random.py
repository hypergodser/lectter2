import random 

print("Random number between 1 and 10:", random.randint(1, 10))
nynumber = random.randint(1, 10)
ntries = 1
you = -1
while ntries <= 5 and you != nynumber:
    you = int(input("Guess the number between 1 and 10: "))
    if you < nynumber:
        print("Too low!")
    elif you > nynumber:
        print("Too high!")
    ntries += 1