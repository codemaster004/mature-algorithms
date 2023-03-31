
def calculate_change(change):
	available_bills = [200, 100, 50, 20, 10, 5, 2, 1]
	i = 0
	while change > 0:
		if change >= available_bills[i]:
			number_of_bills = change // available_bills[i]
			change = change - (available_bills[i] * number_of_bills)
			print(available_bills[i], "x", number_of_bills)
		i += 1


if __name__ == '__main__':
	calculate_change(400)
	calculate_change(138)
	calculate_change(13)
