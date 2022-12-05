def part1(in_file):
    cases = {
        "A X" : 4, 
        "A Y" : 8,
        "A Z" : 3,
        "B X" : 1,
        "B Y" : 5,
        "B Z" : 9,
        "C X" : 7,
        "C Y" : 2,
        "C Z" : 6,
    }
    
    with open(in_file) as inp:
        
        score = 0
        for round in inp:
            round = round.rstrip('\n')
            score+=cases[round]
        
    print(score)
    
def part2(in_file):
    cases = {
        "A X" : 3, 
        "A Y" : 4,
        "A Z" : 8,
        "B X" : 1,
        "B Y" : 5,
        "B Z" : 9,
        "C X" : 2,
        "C Y" : 6,
        "C Z" : 7,
    }
    
    with open(in_file) as inp:
        
        score = 0
        for round in inp:
            round = round.rstrip('\n')
            score+=cases[round]
        
    print(score)
    
#part1("day2inp.txt")
part2("day2inp.txt")
    