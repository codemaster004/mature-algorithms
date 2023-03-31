import math


def greatest_common_divisor1(a, b):
	while a != b:
		if a > b:
			a -= b
		else:
			b -= a
	return a


def greatest_common_divisor2(a, b):
	while b != 0:
		a, b = b, a
		b = b % a
	return a


if __name__ == '__main__':
	print(greatest_common_divisor1(12, 16))
	print(greatest_common_divisor2(16, 12))
	
	print(math.gcd(12, 16))
