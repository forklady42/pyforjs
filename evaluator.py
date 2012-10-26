"""
Evaluates syntax tree for basic arithmetic and variable assignment.
"""

variables = {}
operators = {'+': lambda l,r: evaluate(l)+evaluate(r),
			 '-': lambda l,r: evaluate(l)-evaluate(r),
			 '*': lambda l,r: evaluate(l)*evaluate(r),
			 '/': lambda l,r: evaluate(l)/evaluate(r),
			 '=': lambda l,r: variables.__setitem__(evaluate(l), evaluate(r))
			 }


def evaluate(parser_tree):
	if parser_tree['type'] == 'number':
		return int(parser_tree['value'])
	elif parser_tree['type'] in operators:
		return operators[parser_tree['type']](parser_tree['left'], parser_tree['right'])
	elif parser_tree['type'] == '-u':
		return -1*evaluate(parser_tree['right'])
	elif parser_tree['type'] == 'identifier':
		variables[parser_tree['value']]=''
		return parser_tree['value']
	else:
		return "Unknown type"

def eval(parser_tree):
	value = evaluate(parser_tree)
	if value == None:
		return variables
	return value
	

if __name__ == "__main__":
    #tree = {'left': {'type': 'identifier', 'value': 'x'}, 'type': '=', 'right': {'type': 'number', 'value': 12}}
    #tree = {'right': {'right': {'type': 'number', 'value': 6}, 'type': '+', 'left': {'type': 'number', 'value': 12}}, 'type': '*', 'left': {'type': 'number', 'value': '4'}}
    #tree = {'right': {'type': 'number', 'value': '12'}, 'type': '-u'}
    tree = {'right': {'right': {'type': 'number', 'value': '2'}, 'type': '+', 'left': {'type': 'number', 'value': '3'}}, 'type': '=', 'left': {'type': 'identifier', 'value': 'x'}}
    
    print evaluate(tree)
    #print variables