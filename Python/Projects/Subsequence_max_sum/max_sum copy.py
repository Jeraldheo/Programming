


def sequence_max_sum(seq):
    max_sum = seq[0]
    curr_sum = seq[0]
    for i in range(1, len(seq)):
        if curr_sum + seq[i] >= seq[i]:
            curr_sum = curr_sum + seq[i]
        else:
            curr_sum = seq[i]
        
        if curr_sum > max_sum:
            max_sum  = curr_sum
    print(max_sum)





sequence = [int(element) for element in input().split()]
sequence_max_sum(sequence)