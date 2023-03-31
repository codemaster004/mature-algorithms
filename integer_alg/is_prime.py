
def is_prime(n):
	if n < 2:
		return False
	
	i = 2
	while i*i <= n:
		if n % i == 0:
			return False
		i += 1
	
	return True

if __name__ == '__main__':
	print(is_prime(13))
	print(is_prime(2))
	print(is_prime(4))
