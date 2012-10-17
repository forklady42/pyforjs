import re

tokens =[]
user_input = raw_input("code:")

for char in user_input:
	if re.match('[+\-*\/\^%=(),]', char):
		tokens.append(['operator', char])
	elif re.match('[0-9]', char):
		tokens.append(['number', char])
	elif re.match('\s', char):
		tokens.append(['whitespace', char])
	else:
		tokens.append(['other', char])

prev = tokens[0]
tmp = []

for i in tokens[1:]:
	#if i[0] == 'operator':
	#	tmp.append(prev)
	#	prev = i
	#elif i[0] == 'number':
	#	if prev[0] == 'number':
	#		prev = ['number', ''.join([prev[1], i[1]])]
	#	else:
	#		tmp.append(prev)
	#		prev = i
	#elif i[0] == 'whitespace':
	#		tmp.append(prev)
	#		prev = i
	#else:
	#	if prev[0] == 'other':
	#		prev = ['other', ''.join([prev[1], i[1]])]
	#	else:
	#		tmp.append(prev)
	#		prev = i

	"""if 'type' - first element of list element within tokens list, equals 'number' or 'other', check to see that previous type 
	equals current type. if so, set previous to list where first element = current type and the second element = the previous value
	concaenated with the current value. otherwise, add the previous list to temporary list and set the previous list to the current list"""

	if i[0] == 'number' or i[0] == 'other':
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

print tokens