import parser
import interpreter
import unittest

class TestParser(unittest.TestCase):

    def testParser(self):
        
        #assignment
        tokens = [['identifier', 'var'],['identifier', 'x'],['operator', '='],['number', '2'],['end', ';']]
        tree = {'right': {'type': 'number', 'value': '2'}, 'type': '=', 'left': {'type': 'identifier', 'value': 'x'}}
        self.assertEqual(parser.parse(tokens), tree)
        
        #addition
        tokens = [['number', '6'],['operator', '+'],['number', '1'],['end', ';']]
        tree = {'right': {'type': 'number', 'value': '1'}, 'type': '+', 'left': {'type': 'number', 'value': '6'}}
        self.assertEqual(parser.parse(tokens), tree)
        
        #compound operations
        tokens = [['identifier', 'var'], ['identifier', 'y'], ['operator', '='], ['number', '6'],['operator', '*'], ['operator', '('], ['number', '8'], ['operator', '+'], ['number', '4'], ['operator', ')'], ['operator', '-'], ['number', '2'], ['end', ';']]
        tree = {'right': {'right': {'type': 'number', 'value': '2'}, 'type': '-', 'left': {'right': {'right': {'type': 'number', 'value': '4'}, 'type': '+', 'left': {'type': 'number', 'value': '8'}}, 'type': '*', 'left': {'type': 'number', 'value': '6'}}}, 'type': '=', 'left': {'type': 'identifier', 'value': 'y'}}
        self.assertEqual(parser.parse(tokens), tree)
        
    def testInterpreter(self):
        
        #variable assignment and addition
        code = 'var x = 7 + 8;'
        eval = {'x': 15}
        self.assertEqual(interpreter.main(code), eval)
        
        #parentheses
        code = '(1+2)/3;'
        eval = 1
        self.assertEqual(interpreter.main(code), eval)
        
        #order of operations and multi-digit numbers
        code = '10*3+4/2;'
        eval = 32
        self.assertEqual(interpreter.main(code), eval)
        
        #Missing semi-colon
        code = '4+3'
        eval = 'Syntax error. Expecting ;'
        self.assertEqual(interpreter.main(code), eval)
        
        #  ***Fix this error message***
        code = 'var x 3;'
        eval = 'Invalid token. Number expected...'
        #eval = 'Invalid token. Must assign variable'
        self.assertEqual(interpreter.main(code), eval)
        
        code = '5 5;'
        eval = 'Invalid token. Number expected...'
        #eval = 'Syntax error.'
        self.assertEqual(interpreter.main(code), eval)

unittest.main()