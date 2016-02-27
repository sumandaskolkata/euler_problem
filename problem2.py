def isEven(num):
	return num%2 == 0

def fibonacci(first,second,sum):

	if (second+first) >4000000:
		return sum
	else: 
		temp = first
		first = second
		second = temp+ second
		if isEven(second):
			sum+=second
		# print second 
		return fibonacci(first,second,sum)


print fibonacci(1,2,2)