#00089333
import random
import os
os.system('cls')


dials = int(input("Each lock has how many dials? "))#Takes in how many dials
if dials < 3:
    print("Your number of dials must be 3 or more.")

list_of_numbers = []
combinations = int(input("How many combinations should I generate? "))#How many combinations to make 
range_ = range(1, dials + 1)
for item in range_:
    list_of_numbers.append(item)
    
min = 0
max = 10
random_list = []

print("\n---------------")
x = 1
while x < combinations + 1:#This makes each 'Number x: ------""
    for y in list_of_numbers:
        y = random.randrange(min, max)
        random_list.append(y)
    print(f'Number {x}: {random_list}')
    x = x + 1
    random_list.clear()#clears my list for it to be reset 

print("---------------")

# I could not figure out this quick enough with the functions, I tried my best

