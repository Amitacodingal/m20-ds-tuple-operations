
#activity1
#Create a tuple with different data types
tuplex = ("tuple", False, 3.2, 1)
print(tuplex)

#create a tuple
tuplex = (4, 6, 2, 8, 3, 1) 
print(tuplex)
#tuples are immutable, so you can not add new elements
#using merge of tuples with the + operator you can add an element and it will create a new tuple
tuplex = tuplex + (9,)
print(tuplex)

#Counts the number of occurrences of item 50 from a tuple
tuple1 = (50, 10, 60, 70, 50)
print(tuple1.count(50))

#create a tuple
tuplex = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
#used tuple[start:stop] the start index is inclusive and the stop index
sliced_tuple = tuplex[3:5]
#is exclusive
print(sliced_tuple)
#if the start index isn't defined, is taken from the beginning of the tuple
sliced_tuple = tuplex[:6]
print(sliced_tuple)


#activity2
# function to check whether palindrome or not
def palind(r):
	e = len(r) -1
	s = 0
	while(s<e):
		if(r[s]!=r[e]):
			return False
		s+=1
		e-=1
	return True


r = (1,2,3,3,2,1)

if(palind(r)):
	print("The Tuple is Flip-Flop")
else:
	print("The Tuple is not Flip-Flop")
 
 
#activity3
weather=(1,0,0,0,1,1,0)
sunny=0
rainy=0
for i in range(0,7):
    if(weather[i]==0):
        rainy+=1
    else:
        sunny+=1

    if(sunny>rainy):
        print("Good weather")
    else:
        print("Bad weather")

#Activty4
def tuple_average(t):
    if len(t) == 0:
        return 0  # Return 0 for an empty tuple to avoid division by zero
    return sum(t) / len(t)

# Example tuple
my_tuple = (10, 20, 30, 40, 50)

# Calculate and print the average
average = tuple_average(my_tuple)
print("The average of the tuple is:", average)

#acp
from functools import reduce

def product_of_tuple(tup):
    return reduce(lambda x, y: x * y, tup)

# Test tuples
tup1 = (4, 3, 2, 2, -1, 18)
tup2 = (2, 4, 8, 8, 3, 2, 9)

# Calculate and print products
print("Tuple 1:", tup1)
print("Product of Tuple 1:", product_of_tuple(tup1))

print("\nTuple 2:", tup2)
print("Product of Tuple 2:", product_of_tuple(tup2))




