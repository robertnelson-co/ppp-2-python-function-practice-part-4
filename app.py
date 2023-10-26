#function called max_num() to find the maximum of three numbers 
def max_num(arg1, arg2, arg3):
    biggie = max(arg1, arg2, arg3)
    print(f"the biggest number among {arg1}, {arg2}, and {arg3} is {biggie}")

max_num(1,1.3,0.9)
#function called mult_list() to multiply all the numbers in a list

def mult_list(number_list):
    result = 1
    for num in number_list:
        result *= num
    print(f"After multiplying all the numbers in {number_list}, the result is {result}")

number_list = {1, 2, 3}
mult_list(number_list)
#function called rev_string() to reverse a string

def rev_string(input):
    reversed_string = input [::-1]
    print(reversed_string)

rev_string("hello")

#function called num_within() to check whether a number falls in a given range
#Accepts number, begining of range, and end of range(inclusive) as arguments
#Examples: num_within(3,2,4) returns true;  num_within(10,2,5) returns false

#function called pascal() that prints out the first n rows of Pascal's triangle
#Accepts number n, the number of rows to print
