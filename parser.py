"""
Basic parser for mathematical expressions in javascript.
"""


class Token:
    """
    Keeps track of the tokens and the current position in the list of tokens.
    """

    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = tokens[0]
        self.counter = 0
        self.error = []

    def read_next_token(self):
        self.counter+=1
        if len(self.tokens) > self.counter:
            self.current_token = self.tokens[self.counter]
        else:
            self.error.append("Syntax error. Expecting ;")
            self.current_token = ["end", ";"]

def nud(tokens):
    if tokens.current_token[0] == 'identifier':
        if tokens.current_token[1] in keywords:
            return keywords[tokens.current_token[1]](tokens)
    left = {'type': tokens.current_token[0], 'value': tokens.current_token[1]}
    return left

def op(tokens, l, t):
    """
    Parses the left and right trees of a binary operator and returns the combined tree.
    """
    
    tree = {'type':t[1], 'left': l, 'right': expression(tokens, op_symbols[t[1]]['lbp'])}
    return tree


def neg(tokens, right, t):
    tree = {'type':t[1], 'right': right}
    return tree

def var(tokens):
    #tokens.read_next_token()
    if tokens.tokens[tokens.counter + 1][0] != "identifier":
        tokens.error.append('Variable must follow declaration.')


#Global lookup dictionaries
op_symbols = {'+': {'lbp':10, 'led':op}, '/':{'lbp':20, 'led':op}, '*':{'lbp':20, 'led':op}, '-':{'lbp':10, 'led':op}, 
              '-u':{'lbp':1, 'led':neg}, '=':{'lbp':5, 'led':op}}
symbols = {'number':{'lbp':1, 'nud': nud, 'led':nud } ,'operator':op_symbols, 'end':{'lbp':0}, 'identifier':{'lbp':1, 'nud':nud}}
keywords = {'var': var }

def paren(tokens):
    value = expression(tokens, 0)

    if tokens.current_token[1] != ")":
        tokens.error.append("Expecting closing parenthesis")

    return value


def expression(tokens, rbp=0):
    """
    Takes in a token object and an optional right binding power. Traverses the token's
    list of tokens, recursively building a tree. Returns the tree.
    """
    global op_symbols #, symbols
    
    t = tokens.current_token
    
    try:
        left = symbols[t[0]]['nud'](tokens)
    
        return traverse(tokens, left, rbp)    

    except KeyError:
        if tokens.current_token[1] == "-":
            tokens.current_token[1] = "-u"
            t = tokens.current_token

            tokens.read_next_token()

            try:
                right = symbols[tokens.current_token[0]]['nud'](tokens)
            except KeyError:
                tokens.read_next_token()
                right = paren(tokens)

            left = symbols[t[0]][t[1]]['led'](tokens, right, t)
            return traverse(tokens, left, rbp)
        elif tokens.current_token[1] == "(":
            t = tokens.current_token
            tokens.read_next_token()
            left = paren(tokens)
            
            return traverse(tokens, left, rbp)
        else:          
            tokens.error.append("Invalid token. Number expected...")

def traverse(tokens, left, rbp):
    """
    Recursively traverses list of tokens along with expression(). Looks up operators
    in op_symbols and calls the appropriate function to recursively build the left 
    and right tree of each operator.
    Returns tree.
    
    """
    
    global op_symbols

    tokens.read_next_token()

    if tokens.current_token[0] == 'identifier':
        return expression(tokens, rbp)    

    try:
        lbp = symbols[tokens.current_token[0]]['lbp']
    except KeyError:
        if tokens.current_token[1] == ")":
            return left
        else:
            lbp = symbols[tokens.current_token[0]][tokens.current_token[1]]['lbp']


    while rbp < lbp:
        t = tokens.current_token
        tokens.read_next_token()

        left = symbols[t[0]][t[1]]['led'](tokens, left, t)
        
        try:
            lbp = symbols[tokens.current_token[0]]['lbp']
        except KeyError:
            if tokens.current_token[1] == ")":
                return left
            else:
                lbp = symbols[tokens.current_token[0]][tokens.current_token[1]]['lbp']

    return left

def parse(t):
    
    """
    Takes in a list of functions and applies the appropriate functions
    to build and return the parse tree or return an error.
    """

    token = Token(t)
    temp = expression(token)
    if token.error == []:
        return temp
    return token.error[0]

if __name__ == "__main__":
    #t = [['identifier', 'var'],['identifier', 'x'],['operator', '='],['number', '2'],['end', ';']]
    #t = [['identifier', 'var'],['identifier', 'x'], ['operator', '='], ['number', '3'], ['operator', '+'], ['number', '2'],['end', ';']]
    t=[['identifier', 'var'], ['identifier', 'y'], ['operator', '='], ['number', '6'],['operator', '*'], ['operator', '('], ['number', '8'], ['operator', '+'], ['number', '4'], ['operator', ')'], ['operator', '-'], ['number', '2'], ['end', ';']]
    print parse(t)