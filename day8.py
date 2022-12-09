def get_rows_cols(inp):
    row_ct = 0
    rows = []
    columns = []
    for row in inp:
        rows.append([])
        row = row.strip('\n')
        for column in range(0,len(row)):
            if len(columns) == column:
                columns.append([int(row[column])])
            else:
                columns[column].append(int(row[column]))
            rows[row_ct].append(int(row[column]))
        row_ct+=1
    return [rows, columns]

def part1(inp_file):
    with open(inp_file) as inp:
        rows,columns = get_rows_cols(inp)
        out_trees = len(rows) * 2 + (len(columns) - 2) * 2
        vis_trees = out_trees
        for i in range(1,(len(rows))-1):
            for j in range(1,len(columns)-1):
                left = rows[i][0:j]
                right = rows[i][(j+1):len(columns)]
                above = columns[j][0:i]
                below = columns[j][(i+1):len(columns)]
                if max(left) < columns[j][i] or \
                    max(right) < columns[j][i] or \
                        max(above) < columns[j][i] or \
                            max(below) < columns[j][i]:
                    vis_trees += 1
    print(vis_trees)
    
def part2(inp_file):
    with open(inp_file) as inp:
        rows,columns = get_rows_cols(inp)
        max_scen_score = 0
        for i in range(1,(len(rows))-1):
            for j in range(1,len(columns)-1):
                left = rows[i][0:j]
                cant_see_left = [index for index, tree in enumerate(left) if tree >= columns[j][i]]
                if len(cant_see_left) == 0:
                    see_left = len(left)
                else:
                    see_left = len(left)-cant_see_left[len(cant_see_left)-1]
                right = rows[i][(j+1):len(columns)]
                cant_see_right = [index for index, tree in enumerate(right) if tree >= columns[j][i]]
                if len(cant_see_right) == 0:
                    see_right = len(right)
                else:
                    see_right = len(right[0:cant_see_right[0]+1])
                above = columns[j][0:i]
                cant_see_above = [index for index, tree in enumerate(above) if tree >= columns[j][i]]
                if len(cant_see_above) == 0:
                    see_above = len(above)
                else:
                    see_above = len(above)-cant_see_above[len(cant_see_above)-1]
                below = columns[j][(i+1):len(columns)]
                cant_see_below = [index for index, tree in enumerate(below) if tree >= columns[j][i]]
                if len(cant_see_below) == 0:
                    see_below = len(below)
                else:
                    see_below = len(below[0:cant_see_below[0]+1])
                scenic_score = see_left*see_right*see_above*see_below
                if scenic_score > max_scen_score:
                    max_scen_score = scenic_score
    print(max_scen_score)
part2("day8inp.txt")
            