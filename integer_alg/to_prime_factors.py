
def to_prime_factors(number):
	i = 2
	while number > 1:
		if number % i == 0:
			print(i)
			number //= i
		else:
			i += 1


if __name__ == '__main__':
	to_prime_factors(12)
