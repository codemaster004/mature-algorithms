from random import randint


def selection_sort(table):
	for i in range(len(table) - 1):
		k = i
		for j in range(i+1, len(table)):
			if table[j] < table[k]:
				k = j
		table[i], table[k] = table[k], table[i]
	return table
	
	
if __name__ == '__main__':
	unsorted_list = [randint(1, 10) for _ in range(11)]
	print(selection_sort(unsorted_list))
