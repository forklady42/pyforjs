import re

def get_tokens():

	tokens =[]

	user_input = raw_input("code:")

	for char in user_input:
		if re.match('[+\-*\/\^%=(),]', char):
			tokens.append(['operator', char])
		elif re.match('[0-9]', char):
			tokens.append(['number', char])
		elif re.match('\s', char):
			tokens.append(['whitespace', char])
		elif re.match(';', char):
			tokens.append(['end', char])
		elif re.match('[a-zA-Z]', char):
			tokens.append(['identifier', char])
		else:
			tokens.append(['other', char])

	prev = tokens[0]
	tmp = []

	for i in tokens[1:]:
		
		if i[0] == 'number' or i[0] == 'other' or i[0]== 'identifier':
			if prev[0] == i[0]:
				prev = [i[0], ''.join([prev[1], i[1]])]
			else:
				tmp.append(prev)
				prev = i
		else:
			tmp.append(prev)
			prev = i

	tmp.append(prev)
	tokens = tmp

	return tokens

if __name__ == "__main__":
	print get_tokens()