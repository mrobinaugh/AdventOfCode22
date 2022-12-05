input = open("day1Input.txt")
fat_elf = 0;
most_cal = 0;
elf = 0
total = 0
for item in input:
    if item == "\n":
        if total > most_cal:
            most_cal = total
            fat_elf = elf
        ++elf
        total = 0
    else:
        total += int(item)
        
print(most_cal)
        