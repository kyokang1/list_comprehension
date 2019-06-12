#total_comprehension.py

my_numbers = [1, 2, 3, 4, 5, 6, 7]
print("--------------")
print("ORIGINAL LIST:", my_numbers)

print("--------------")
print("TOTAL COMPREHENSION...")

# TODO: write python code here

##
##

#1. Use mapping capabilities to multiply each number by 100 (e.g. [100, 200, 300, 400, 500, 600, 700])

#1-1. using map()
def enlarge(i):
    return i * 100

my_numbers1 = map(enlarge, my_numbers)

print("--------------")
print("MAPPED LIST: ", list(my_numbers1))

#1-2. using for ... in ...
#my_numbers1 = []
#
#for i in my_numbers:
#    my_numbers2.append(i*100)
#
#print("--------------")
#print("MAPPED LIST: ", list(my_numbers1))

#1-3. using list comprehension
#my_numbers1 = [i * 100 for i in my_numbers]
#
#print("--------------")
#print("MAPPED LIST: ", my_numbers1)

##
##

#2. Use filtering capabilities to return only the numbers greater than three (e.g. [4, 5, 6, 7])

#2-1. using filter() function
def larger_than_three(i):
    return i > 3

print("--------------")
print("FILTERED LIST W/ MATCHES: ", list(filter(larger_than_three, my_numbers)))

#2-1-1. 
#my_numbers3 = filter(larger_than_three, my_numbers)
#print("--------------")
#print("FILTERED LIST W/ MATCHES: ", list(my_numbers3))

#2-2. using lambda
#print("--------------")
#print("FILTERED LIST W/ MATCHES: ", list(filter(lambda i: i > 3, my_numbers)))

#2-3. Professor's solution
filtered_list = [n for n in my_numbers if n > 3]
print("--------------")
print("FILTERED LIST W/ MATCHES: ", filtered_list)  #filter_list is defined as list so list() is not needed

##
##

#3. Use filtering capabilities to return only the numbers greater than eight (e.g. [])

#3-1. using filter() function
#def larger_than_eight(i):
#    return i > 8
#
#print("--------------")
#print("FILTERED LIST W/O MATCHES: ", list(filter(larger_than_eight, my_numbers)))

#3-2. using lambda
print("--------------")
print("FILTERED LIST W/O MATCHES: ", list(filter(lambda i: i > 8, my_numbers)))

#3-3. Professor's solution
no_matches = [n for n in my_numbers if n > 8]
print("--------------")
print("FILTERED LIST W/O MATCHES:", no_matches) #> [4, 5, 6, 7]

##
##

#4. Use mapping and filtering capabilities to return only the numbers greater than three, each multiplied by 100 (e.g. [400, 500, 600, 700])

#4-1. using filter() function
my_numbers4 = filter(larger_than_three, my_numbers)
my_numbers4 = map(enlarge, my_numbers4)

print("--------------")
print("MAPPED AND FILTERED LIST: ", list(my_numbers4))

#4-2. using lambda
#my_numbers4 = map(enlarge, my_numbers)
#
#print("--------------")
#print("MAPPED AND FILTERED LIST: ", list(filter(lambda i: i > 300, my_numbers4)))

#4-3. Professor's solution
last_list = [n * 100 for n in my_numbers if n > 3]
print("--------------")
print("MAPPED AND FILTERED LIST:", last_list) #> [400, 500, 600, 700]

