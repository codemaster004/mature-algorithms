from random import randint


def insertion_sort(table):
	for i in range(len(table)):
		temp = table[i]
		j = i - 1
		while j >= 0 and table[j] > temp:
			table[j+1] = table[j]
			j -= 1
		table[j+1] = temp
	return table


if __name__ == '__main__':
	unsorted_list = [randint(1, 10) for _ in range(11)]
	print(insertion_sort(unsorted_list))
