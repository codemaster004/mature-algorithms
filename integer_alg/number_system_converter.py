
# BIN2DEC
def to_decimal(number, system_base=2):
	result = 0
	for char in number:
		result = result * system_base + int(char)
	print(result)


# DEC2BIN
def from_decimal(number, system_base=2):
	number = int(number)
	table = []
	
	while number >= 1:
		table.append(number % system_base)
		number //= system_base
	
	print(*table[::-1], sep='')


if __name__ == '__main__':
	to_decimal('110')
	from_decimal('6')
