input = open("day1Input.txt")
cals= []
elf = 0
total = 0
for item in input:
    if item == "\n":
        cals.append(total)
        ++elf
        total = 0
    else:
        total += int(item)
        
cals.sort(reverse=True)
top3tot = cals[0] + cals[1] + cals[2]
        
print(top3tot)
        