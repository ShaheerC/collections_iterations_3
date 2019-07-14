#EXERCISE 11
print("===START OF EXERCISE 11===")

#11
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

#12
print("How many pizzas do you want to order?")
quantity = int(input())
quantity += 1

for pizza in range (1, quantity):
    print("How many toppings for pizza {}?".format(pizza))
    topping = int(input())
    print('You have ordered a pizza with {} toppings.'.format(topping))
    
if quantity < 2:
    print("Get outta me store if you ain't ordering any pizza!")
else:
    print('Thank you for your order of {} pizzas! Enjoy'.format(quantity - 1))