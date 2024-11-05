def move_zeros(numbers):
    zeros = 0 #to count the zeros
    new_list = [] #create the new list with the new order
    for i in numbers:
        if i == 0: #if the item is zero add one the the count
            zeros += 1
        else: #if not add the number to the new list
            new_list.append(i)
    print(zeros)
    for i in range (zeros): # add zero (count of zero in the initial list) time
        new_list.append(0)
    return new_list

print(move_zeros([0,1,3,0,0,0,0,0,4,5,0,0,1,2,10,0,0]))
