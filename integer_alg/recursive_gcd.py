
def recursive_gcd1(a, b):
	if a != b:
		if a > b:
			return recursive_gcd1(a-b, b)
		else:
			return recursive_gcd1(a, b-a)
	return a

def recursive_gcd2(a, b):
	if b != 0:
		return recursive_gcd2(b, a%b)
	return a


if __name__ == '__main__':
	print(recursive_gcd1(12, 16))
	print(recursive_gcd2(12, 16))
