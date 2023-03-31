
def is_perfect(number):
	sum_d = 1
	
	i = 2
	while i*i < number:
		if number % i == 0:
			sum_d = sum_d + i + number // i
		i += 1
	if i*i == number:
		sum_d = sum_d + i
	
	return number == sum_d


if __name__ == '__main__':
	print(is_perfect(6))
	print(is_perfect(5))
    
