def part1(inp_file):
    cont_pairs = 0
    with open(inp_file) as inp:
        for pair in inp:
            pair = pair.rstrip('\n')
            set1start = int(pair[0:pair.index('-')])
            set1end = int(pair[pair.index('-')+1:pair.index(',')]) + 1
            set2start = int(pair[pair.index(',')+1:pair.rindex('-')]) 
            set2end = int(pair[pair.rindex('-')+1:]) + 1
            set1 = set(range(set1start,set1end))
            set2 = set(range(set2start,set2end))
            intersect = set(set1 & set2)
            if len(intersect) == len(set1) or len(intersect) == len(set2):
                cont_pairs+=1
    print("Task 1 result:" , cont_pairs)   
    
def part2(inp_file):
    cont_pairs = 0
    with open(inp_file) as inp:
        for pair in inp:
            pair = pair.rstrip('\n')
            set1start = int(pair[0:pair.index('-')])
            set1end = int(pair[pair.index('-')+1:pair.index(',')]) + 1
            set2start = int(pair[pair.index(',')+1:pair.rindex('-')]) 
            set2end = int(pair[pair.rindex('-')+1:]) + 1
            set1 = set(range(set1start,set1end))
            set2 = set(range(set2start,set2end))
            intersect = set(set1 & set2)
            if len(intersect) > 0:
                cont_pairs+=1
    print("Task 2 result:" , cont_pairs)       
    
part1("day4inp.txt")    
part2("day4inp.txt")
