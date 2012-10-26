import lexer
import parser
import evaluator

def main():
	tokens = lexer.get_tokens()

	parser_tree = parser.parse(tokens)

	if type(parser_tree) == str:
		print parser_tree
	else:
		print evaluator.eval(parser_tree)


if __name__ == '__main__':
	main()