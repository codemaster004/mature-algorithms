from random import randint


def search_for_min_max(search_table):
	i = 2
	
	if search_table[0] > search_table[1]:
		found_min = search_table[1]
		found_max = search_table[0]
	else:
		found_min = search_table[0]
		found_max = search_table[1]
	
	while i + 2 <= len(search_table):
		if search_table[i] > search_table[i + 1]:
			if search_table[i] > found_max:
				found_max = search_table[i]
			if search_table[i + 1] < found_min:
				found_min = search_table[i+1]
		else:
			if search_table[i + 1] > found_max:
				found_max = search_table[i+1]
			if search_table[i] < found_min:
				found_min = search_table[i]
		i += 2
	
	if len(search_table) % 2 == 1:
		if search_table[i] > found_max: 
			found_max = search_table[i]
		if search_table[i] < found_min: 
			found_min = search_table[i]
	
	return found_min, found_max

if __name__ == '__main__':
	randomised_table = [randint(0, 100) for _ in range(11)]
	print(search_for_min_max(randomised_table))
	print(min(randomised_table), max(randomised_table))
