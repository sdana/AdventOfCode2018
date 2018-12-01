import sys

file_path = "./Day1Input.txt"
input_numbers = open(file_path).read().splitlines()

# print(int(input_numbers))

# input_numbers = [7, 7, -2, -7, -4]

frequency = 0
calibrate = []

print("Calibrating...")
for i in range(len(input_numbers)*2):
    for num in input_numbers:
        # print("current: " + str(frequency) + "input: " + str(num))
        frequency += int(num)
        # print("result: " + str(frequency))
        if frequency in calibrate:
            print("Found Calibration: ", frequency)
            exit()
        else:
            calibrate.append(frequency)