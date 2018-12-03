import string

file_loc = "./input"

input_file = open(file_loc).read().splitlines()

alpha = string.ascii_lowercase

two_count = 0
three_count = 0

for i in input_file:
    has2 = 0
    has3 = 0
    print(i)
    for n in alpha:
        print(n)
        count = i.count(n)
        if count == 3 and has3 == 0:
            print("Three " + n)
            two_count += 1
            has3 += 1
        elif count == 2 and has2 == 0:
            print("Two " + n)
            three_count += 1
            has2 += 1
checksum = two_count * three_count

print("Twos: " + str(two_count))
print("Threes: " + str(three_count))
print("Checksum is " + str(checksum))