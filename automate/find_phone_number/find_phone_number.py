#! python3

# 123-456-5678


def is_phone_numer(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True


global_count = 0
message = "This is 123-456-5678a text of 123-456-5678 for test"
for i in range(len(message)):
    phone = message[i:i + 12]
    if is_phone_numer(phone):
        global_count += 1
print(global_count)
