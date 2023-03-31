
def fibonacci_sequence(number):
	first_number = 1
	second_number = 1
	
	if number > 2:
		for i in range(3, number+1):
			new_number = first_number + second_number
			first_number = second_number
			second_number = new_number
	
	return second_number


def recursive_fib(number):
	if number < 3:
		return 1
	return recursive_fib(number - 2) + recursive_fib(number - 1)


if __name__ == '__main__':
	print(fibonacci_sequence(1))
	print(recursive_fib(2))
	print(fibonacci_sequence(3))
	print(recursive_fib(4))
	print(fibonacci_sequence(5))
	print(recursive_fib(6))
	print(fibonacci_sequence(7))
	print(recursive_fib(8))
