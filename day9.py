def make_move(pos_t, pos_h, prev_mv, l_h):
    x_dist = abs(pos_h[0]-pos_t[0])
    y_dist = abs(pos_h[1]-pos_t[1])
    move = [0,0]
    if x_dist > 1 or y_dist > 1:
        if abs(prev_mv[0]) > 0 and abs(prev_mv[1]) > 0:
            if pos_h[0] == pos_t[0]:
                move[1] = prev_mv[1]
            elif pos_h[1] == pos_t[1]:
                move[0] = prev_mv[0]
            else:
                move = prev_mv[0:2]
        else:
            move[0] = l_h[0] - pos_t[0]
            move[1] = l_h[1] - pos_t[1]
    return move

def part1(inp_text):
    with open(inp_text) as inp:
        pos_h = [0,0]
        last_h = [0,0]
        pos_t = [0,0]
        t_poses = {str(pos_t[0]) + ',' + str(pos_t[1])}
        for move in inp:
            move = move.strip('\n')
            direc, cnt = move.split(' ')
            for i in range(0,int(cnt)):
                if direc == 'R':
                    pos_h[0] += 1
                elif direc == 'L':
                    pos_h[0] -= 1
                elif direc == 'U':
                    pos_h[1] += 1
                elif direc == 'D':
                    pos_h[1] -= 1
                x_dist = abs(pos_h[0]-pos_t[0])
                y_dist = abs(pos_h[1]-pos_t[1])
                if x_dist > 1 or y_dist > 1:
                    pos_t[0:2] = last_h[0:2]
                    t_poses.add(str(pos_t[0]) + ',' + str(pos_t[1]))
                last_h[0:2] = pos_h[0:2]

        print(len(t_poses))
        
def part2(inp_text):
    with open(inp_text) as inp:
        pos_h = [0,0]
        pos_1 = [0,0]
        pos_2 = [0,0]
        pos_3 = [0,0]
        pos_4 = [0,0]
        pos_5 = [0,0]
        pos_6 = [0,0]
        pos_7 = [0,0]
        pos_8 = [0,0]
        pos_9 = [0,0]
        l_h = [0,0]
        l_1 = [0,0]
        l_2 = [0,0]
        l_3 = [0,0]
        l_4 = [0,0]
        l_5 = [0,0]
        l_6 = [0,0]
        l_7 = [0,0]
        l_8 = [0,0]
        mv_1 = [0,0]
        mv_2 = [0,0]
        mv_3 = [0,0]
        mv_4 = [0,0]
        mv_5 = [0,0]
        mv_6 = [0,0]
        mv_7 = [0,0]
        mv_8 = [0,0]
        mv_9 = [0,0]
        nine_poses = {str(pos_9[0]) + ',' + str(pos_9[1])}
        for line in inp:
            line = line.strip('\n')
            direc, cnt = line.split(' ')
            for i in range(0,int(cnt)):
                if direc == 'R':
                    pos_h[0] += 1
                elif direc == 'L':
                    pos_h[0] -= 1
                elif direc == 'U':
                    pos_h[1] += 1
                elif direc == 'D':
                    pos_h[1] -= 1
                if abs(pos_h[0]-pos_1[0]) > 1 or abs(pos_h[1]-pos_1[1]) > 1:
                    mv_1[0] = l_h[0] - pos_1[0]
                    mv_1[1] = l_h[1] - pos_1[1]
                    pos_1[0:2] = l_h[0:2]
                l_h = pos_h[0:2]
                mv_2 = make_move(pos_2, pos_1, mv_1, l_1)
                pos_2[0] += mv_2[0]
                pos_2[1] += mv_2[1]
                l_1 = pos_1[0:2]
                mv_3 = make_move(pos_3, pos_2, mv_2, l_2)
                pos_3[0] += mv_3[0]
                pos_3[1] += mv_3[1]
                l_2 = pos_2[0:2]
                mv_4 = make_move(pos_4, pos_3, mv_3, l_3)
                pos_4[0] += mv_4[0]
                pos_4[1] += mv_4[1]
                l_3 = pos_3[0:2]
                mv_5 = make_move(pos_5, pos_4, mv_4, l_4)
                pos_5[0] += mv_5[0]
                pos_5[1] += mv_5[1]
                l_4 = pos_4[0:2]
                mv_6 = make_move(pos_6, pos_5, mv_5, l_5)
                pos_6[0] += mv_6[0]
                pos_6[1] += mv_6[1]
                l_5 = pos_5[0:2]
                mv_7 = make_move(pos_7, pos_6, mv_6, l_6)
                pos_7[0] += mv_7[0]
                pos_7[1] += mv_7[1]
                l_6 = pos_6[0:2]
                mv_8 = make_move(pos_8, pos_7, mv_7, l_7)
                pos_8[0] += mv_8[0]
                pos_8[1] += mv_8[1]
                l_7 = pos_7[0:2]
                mv_9 = make_move(pos_9, pos_8, mv_8, l_8)
                if mv_9 != [0,0]:
                    pos_9[0] += mv_9[0]
                    pos_9[1] += mv_9[1]
                    nine_poses.add(str(pos_9[0]) + ',' + str(pos_9[1]))
                l_8 = pos_8[0:2]
                

        print(len(nine_poses))
                    
            
part2("day9inp.txt")