import re

with open('1.input', 'r') as file:
    data = file.readlines()

def calculate_total(data):
    total = 0
    for line in data:
        digits = ''.join(re.findall(r'\d', line.rstrip('\n')))
        calibration_value = digits[0] + digits[-1]
        total += int(calibration_value)
    return total

total = calculate_total(data)
print("Answer part one:", total)

# Part Two
calibration_value= 0
total = 0
digits_text = {
    # Autocomplete dictionary
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}

data2 = data.copy()
number_list = []

for line in data2:
    digits = ''
    #print("line: ",line)
    for position in range(0, line.__len__()):
        for key, value in digits_text.items():
            found = line[position:].find(value) 
            if(found==0):
                digits += str(key)
                #print("new digit", digits)
            if(line[position] == str(key)):
                digits += str(key)
                #print("new digit numeric", digits)
    
    number_list.append(digits)

total = calculate_total(number_list)
print("Answer part two:", total)

# 562226 too high
# 55266 too low