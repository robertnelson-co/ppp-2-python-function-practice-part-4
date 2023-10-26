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

def num_within(number_to_test, start_range, end_range):
    if start_range <= number_to_test <= end_range:
        print("True")
    else:
        print("False")

num_within(29, 1, 30)
num_within(3, 3.1415926535897932384626433, 3.1416)

#function called pascal() that prints out the first n rows of Pascal's triangle
#Accepts number n, the number of rows to print
triangle = [[1], [1,1]]
def pascal(n):
  #check to make sure there's more than one row!
  if n < 1:
    print("add more rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    #fill up correct number of rows in triangle
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      #create correct row, then add to triangle
      length = len(row_prev)+1
      for i in range(length):
        #first number is 1
        if i == 0:
          row.append(1)
        #intermediate nunmbers get added from previous rows
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        #last number is 1
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    #print triangle
    for row in triangle:
      print(row)

pascal(5)
pascal(10)
       