
def factorial(number):
	result = 1
	for i in range(1, number + 1):
		result *= i
	
	return result


def recursive_factorial(number):
	if number > 1:
		return number * recursive_factorial(number - 1)
	elif number == 0 or number == 1: 
		return 1


if __name__ == '__main__':
	print(factorial(5))
	print(recursive_factorial(4))
