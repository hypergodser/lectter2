score = int(input("enter score: "))

while score < 0 or score > 100:
    print("error : the score cannot be nega")
    print ('or less than 0.')
    score = int(input("enter score: "))