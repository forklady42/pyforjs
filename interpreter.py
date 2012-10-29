import lexer
import parser
import evaluator

def main(input):
	tokens = lexer.get_tokens(input)

	parser_tree = parser.parse(tokens)

	if type(parser_tree) == str:
		return parser_tree
	else:
		return evaluator.eval(parser_tree)


if __name__ == '__main__':
    code = raw_input("code:")
    print main(code)