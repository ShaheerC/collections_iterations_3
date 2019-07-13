#EXERCISE 11
print("===START OF EXERCISE 11===")

one_to_hundred = range(1, 101)

for num in one_to_hundred:
    if num % 3 == 0 and num % 5 == 0:
        print ('BitMaker')
    elif num % 3 == 0:
        print ('Bit')
    elif num % 5 == 0:
        print ('Maker')
    else: 
        print (num)

#EXERCISE 12
print("===START OF EXERCISE 12===")