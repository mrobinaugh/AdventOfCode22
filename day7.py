class directory:
    
    def __init__(self, name, parent=None):
        self.parent = parent
        self.name = name
        self.size = 0
        
    def get_name(self):
        return self.name
        
    def get_parent(self):
        return self.parent
        
    def add_size(self,size):
        if self.name != '/':
            self.size += size
            self.parent.add_size(size)
        else:
            self.size += size
            
    def get_size(self):
        return self.size
            
def gen_directories(inp):
    dirs = {}
    dir_names = {}
    for line in inp:
        line = line.strip('\n')
        if line[0] == '$' and line[2:4] == 'cd':
            dollar, cd, loc = line.split(' ')
            if loc == '..':
                curr_dir = curr_dir.get_parent()
            elif loc == '/' and dirs.get(loc) == None:
                dirs[loc] = directory(loc)
                curr_dir = dirs[loc]
            elif dirs.get(loc) == None:
                dirs[loc] = directory(loc,curr_dir)
                dir_names[loc] = 1
                curr_dir = dirs[loc]
            else:
                dirs[loc + str(dir_names[loc])] = directory(loc,curr_dir)
                curr_dir = dirs[loc + str(dir_names[loc])]
                dir_names[loc] += 1
        elif line[0].isdigit():
            size, file_name = line.split(' ')
            curr_dir.add_size(int(size))
    return dirs
        

def part1(inp_text):
    with open(inp_text) as inp:
        dirs = gen_directories(inp)
        small_dir_sum = 0
        for i in dirs:
            dir_size = dirs[i].get_size()
            if dir_size <= 100000:
                small_dir_sum += dir_size
    print("Task 1: ", small_dir_sum)  
    
def part2(inp_text):
    with open(inp_text) as inp:
        dirs = gen_directories(inp)
        curr_choice = dirs['/'].get_size()
        have = 70000000 - curr_choice
        need = 30000000 - have
        for i in dirs:
            curr_size = dirs[i].get_size()
            if curr_size >= need and curr_size <= curr_choice:
                curr_choice = curr_size
        
    print("Task 2: ", curr_choice)           
        
                    
            
                
part2("day7inp.txt")              
            