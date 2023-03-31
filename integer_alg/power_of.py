
def to_the_power_of(base, power=2):
	if power == 0:
		result = 1
	elif power == 1:
		result = base
	else:
		result = 1
		for i in range(power):
			result *= base
	
	return result


if __name__ == '__main__':
	print(to_the_power_of(8))
	print(to_the_power_of(5, 0))
	print(to_the_power_of(13, power=1))
	print(to_the_power_of(2, 5))
