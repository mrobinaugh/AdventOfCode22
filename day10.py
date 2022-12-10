def disp_pix(pixel, x):
    if (x-1) <= pixel and (x+1) >= pixel:
        print('#', end = '')
    else:
        print('.', end = '')

def part1(inp_text):
    with open(inp_text) as inp:
        cycle = 1
        x = 1
        sig_stren = 0
        for line in inp:
            line = line.strip('\n')
            if line[0:4] == "addx":
                add, num = line.split(' ')
                cycle += 1
                if cycle == 20 or (cycle-20)%40 == 0:
                    sig_stren += cycle * x
                x += int(num)
            cycle += 1
            if cycle == 20 or (cycle-20)%40 == 0:
                sig_stren += cycle * x
    
    print("Task 1:", sig_stren)
    
def part1(inp_text):
    with open(inp_text) as inp:
        pixel = 0
        x = 1
        for line in inp:
            disp_pix(pixel, x)
            line = line.strip('\n')
            if line[0:4] == "addx":
                add, num = line.split(' ')
                pixel += 1
                if (pixel) == 40:
                    print('')
                    pixel = 0
                disp_pix(pixel, x)
                x += int(num)
            pixel += 1
            if (pixel) == 40:
                print('')
                pixel = 0
            
part1("day10inp.txt")
                