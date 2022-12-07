def part1(inp_file):
    with open(inp_file) as inp:
        string = inp.readline()
        mark = 4
        for i in range(0,len(string)-mark+1):
            if len(set(string[i:i+mark])) == mark:
                return i+mark
                
def part2(inp_file):
    with open(inp_file) as inp:
        string = inp.readline()
        mark = 14
        for i in range(0,len(string)-mark+1):
            if len(set(string[i:i+mark])) == mark:
                return i+mark
            
            
                
print(part1("day6inp.txt"))
print(part2("day6inp.txt"))