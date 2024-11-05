def move_zeros(numbers):
    zeros = 0
    new_list = []
    for i in numbers:
        if i == 0:
            print(i)
            zeros += 1
        else:
            new_list.append(i)
    print(zeros)
    for i in range (zeros):
        new_list.append(0)
    return new_list

print(move_zeros([0,1,3,0,0,0,0,0,4,5,0,0,1,2,10,0,0]))
    