from random import randint


def binary_search(sorted_list, value):
	start = 0
	end = len(sorted_list) - 1
	
	if sorted_list[start] == value:
		return start
	if sorted_list[end] == value:
		return end
	
	while start <= end:
		mid = int((start + end) / 2)
		if sorted_list[mid] == value:
			return mid
		
		if sorted_list[mid] <= value:
			start = mid + 1
		else:
			end = mid - 1
	
	return -1


if __name__ == '__main__':
	randomised_list = [randint(1, 10) for _ in range(11)]
	randomised_list.sort()
	
	print(randomised_list)
	print(binary_search(randomised_list, 2))
	
