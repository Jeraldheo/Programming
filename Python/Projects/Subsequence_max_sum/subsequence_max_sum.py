


def sequence_max_sum(seq):
    index_max = 0
    sub = [[seq[0],seq[0]]]
    for i in range(1, len(seq)):
        curr_sum = sub[i-1][0] + seq[i]
        if curr_sum >= seq[i]:
            new_sub = [curr_sum]
            new_sub = new_sub + sub[i-1][1:len(sub[i-1])]
            new_sub.append(seq[i])
            sub.append(new_sub)
            if curr_sum > sub[index_max][0]:
                index_max = i
            continue
        
        sub.append([seq[i], seq[i]])
        if seq[i] > sub[index_max][0]:
            index_max = i
    
    print(sub[index_max][0])





sequence = [int(element) for element in input().split()]
sequence_max_sum(sequence)