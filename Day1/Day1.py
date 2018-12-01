file_path = "./Day1Input.txt"
input_numbers = open(file_path).read().splitlines()

frequency = 0
calibrate = []

print("Calibrating...")
for i in range(len(input_numbers)*2):
    for num in input_numbers:
        frequency += int(num)
        if frequency in calibrate:
            print("Found Calibration: ", frequency)
            exit()
        else:
            calibrate.append(frequency)