age_of_myself = 25

for i in range(10):
    guess_age = int(input("guess age:"))
    if guess_age == age_of_myself:
        print("you're right")
        break
    elif guess_age > age_of_myself:
        print("bigger")
    else:
        print("smaller")
print("tired too many times")
