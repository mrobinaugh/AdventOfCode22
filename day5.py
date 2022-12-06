def get_stacks(inp_file):
    with open(inp_file) as inp:
        c = inp.read(1)
        position = 0
        stacks = []
        while True:
            if c.isdigit():
                break
            elif c != '\n':
                is_stack = (position-1) % 4
                if is_stack == 0:
                    stack = (position-1) / 4
                    if c.isalpha():
                        try:
                            stacks[int(stack)].append(c)
                        except:
                            stacks.append([c])
                    else:
                        try:
                            stacks[int(stack)]
                        except:
                            stacks.append([])
                c = inp.read(1)
                position+=1
            else:
                c = inp.read(1)
                position = 0
    return stacks

def part1(inp_file):
    stacks = get_stacks(inp_file)
    with open(inp_file) as inp:
        for moves in inp:
            if moves[0:4] == "move":
                str1, num_moves, str2, from_stack, str3, to_stack = moves.split() 
                for i in range(int(num_moves)):
                    stacks[int(to_stack)-1].insert(0, stacks[int(from_stack)-1].pop(0))
    result = ''
    for stack in stacks:
        if len(stack) > 0:
            result += stack[0]  
              
        
    print("Task 1: ", result)
    
def part2(inp_file):
    stacks = get_stacks(inp_file)
    with open(inp_file) as inp:
        for moves in inp:
            if moves[0:4] == "move":
                str1, num_moves, str2, from_stack, str3, to_stack = moves.split() 
                for i in range(int(num_moves)):
                    stacks[int(to_stack)-1].insert(0+i, stacks[int(from_stack)-1].pop(0))
    result = ''
    for stack in stacks:
        if len(stack) > 0:
            result += stack[0]  
              
        
    print("Task 1: ", result)
    
part1("day5inp.txt")
part2("day5inp.txt")