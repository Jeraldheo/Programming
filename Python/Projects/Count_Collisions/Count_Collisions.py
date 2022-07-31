def count_collisions(directions):
    collisions  = 0
    curr_dir = directions[0]
    con_right = 0
    n  = len(directions)
    for i in range(1, n):
        if curr_dir == 'R':
            curr_dir = directions[i]
            if directions[i]=='L':
                collisions+=2 + con_right
                con_right = 0
                curr_dir = 'S'
            if directions[i] == 'S':
                collisions+=1 + con_right
                con_right = 0
                curr_dir = 'S'
            if directions[i]=='R':
                con_right +=1
        else:
            if curr_dir == 'S':
                curr_dir = directions[i]
                if directions[i] == 'L':
                    curr_dir = 'S'
                    collisions+=1 + con_right
                    con_right = 0
                    
            else:
                curr_dir = directions[i]
    
    return collisions

print(count_collisions("SSRSSRLLRSLLRSRSSRLRRRRLLRRLSSRR"))