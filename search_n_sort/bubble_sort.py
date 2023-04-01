from random import randint


def bubble_sort(table):
	for i in range(len(table)):
		for j in range(1, len(table) - i):
			if table[j - 1] > table[j]:
				table[j - 1], table[j] = table[j], table[j-1]
	return table


if __name__ == '__main__':
	unsorted_list = [randint(1, 10) for _ in range(11)]
	print(bubble_sort(unsorted_list))
