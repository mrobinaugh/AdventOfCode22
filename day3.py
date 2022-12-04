def part1(in_file):
    priority_sum = 0
    inp = open(in_file)
    with open(in_file) as inp:
        for bag in inp:
            stuff = []
            priority_num = 0
            for item in bag[0:int(len(bag)/2)]:
                stuff.append(item)
            for item in bag[int(len(bag)/2):len(bag)]:
                if stuff.count(item) != 0:
                    if item.isupper():
                        priority_num = ord(item) - 38
                    else:
                        priority_num = ord(item) - 96
                    break
            priority_sum += priority_num
    print(priority_sum)
    
def part2(in_file):
    priority_sum = 0
    inp = open(in_file)
    with open(in_file) as inp:
        group = []
        for bag in inp:
            if len(group) != 3:
                group.append(bag)
            if len(group) == 3:
                priority_num = 0
                for item in bag:
                    if group[0].count(item) != 0 and group[1].count(item) != 0:
                        if item.isupper():
                            priority_num = ord(item) - 38
                        else:
                            priority_num = ord(item) - 96
                        break
                priority_sum += priority_num
                group = []
    print(priority_sum)

part2("day3inp.txt")
        