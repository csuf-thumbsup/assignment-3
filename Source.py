def check_word_validity(str, table, endStates):
	state = 0
	
	for char in str:
		if char == 'a':
			col = 0
		elif char == 'b':
			col = 1
		elif char == '$':
			if state in endStates:
				print(str + ' is accepted.')
			else:
				print(str + ' is not accepted.')
		else:
			print('\nInvalid char: ' + char)
			print(str + ' is not accepted.\n')
			return -1
		
		state = table[state][col]


if __name__ == '__main__':

	table = [ [1,2], [1,3], [4,2], [4,4], [4,4] ]
	endStates = [2,3]
	
	with open("data.txt") as file:
		for str in file.readlines():
			check_word_validity(str.strip(), table, endStates)


	
