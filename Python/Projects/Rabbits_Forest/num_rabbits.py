def numRabbits(answers):
    answers.sort()
    num_ans = len(answers)
    curr_ans = 0
    num_rabbits = 0
    while curr_ans<num_ans:
        next_ans = curr_ans + 1
        count = 0
        while (next_ans<num_ans) and (answers[curr_ans]==answers[next_ans]) and (count<answers[curr_ans]):
            count+=1
            next_ans+=1

        num_rabbits+= answers[curr_ans] + 1
        curr_ans = next_ans
    
    return num_rabbits

print(numRabbits([1,1,2]))