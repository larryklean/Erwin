age_of_myself = 25
count = 0

while count < 4:
    guess_age = int(input("guess age:"))
    if guess_age == age_of_myself:
        print("you're right")
        # break
    elif guess_age > age_of_myself:
        print("bigger")
    else:
        print("smaller")
    count += 1
    if count == 3:
        confirm = input("do you want to continue...?")
        if confirm == 'y':
            count = 0
        else:
            break

# print("tried too many times")
