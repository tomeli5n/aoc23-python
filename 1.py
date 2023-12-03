import re

with open('1.input', 'r') as file:
    data = file.readlines()

total = 0
for line in data:
    digits = ''.join(re.findall(r'\d', line.rstrip('\n')))
    calibration_value = digits[0] + digits[-1]
    //print(digits, calibration_value)
    total += int(calibration_value)

print("Answer:", total)
