#implicit type conversion
int_no = 123
float_no = 1.23
sum = int_no + float_no
print("Value:", sum)
print("Data Type:", type(sum))

#explicit type conversion
num_string = '12'
num_int = 23
print("Data type of num_string before typecasting:", type(num_string))

#this is where explicit type conversion happens
num_string = int(num_string)
print("Data type of num_string after typecasting:", type(num_string))

Sum = num_string + num_int
print("The sum is:", Sum)
print("Data type of Sum:", type(Sum))
