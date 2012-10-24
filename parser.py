class Token:

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

def nud(current_token): #this empty string argument was a work around b/c when current token is number. the function that should be called is nud, but the algorithm doesn't seem to consider condidition within while loop?
    left = {'type':current_token[0], 'value':current_token[1]}
    return left

def op(tokens, l, t):
    tree = {'type':t[1], 'left': l, 'right': expression(tokens, op_symbols[t[1]]['lbp'])}
    return tree


def neg(tokens, right, t):
    tree = {'type':t[1], 'right': right}
    return tree

op_symbols = {'+': {'lbp':10, 'led':op}, '/':{'lbp':20, 'led':op}, '*':{'lbp':20, 'led':op}, '-':{'lbp':10, 'led':op}, 
              '-u':{'lbp':1, 'led':neg}, '=':{'lbp':30, 'led':op}}
symbols = {'number':{'lbp':1, 'nud': nud, 'led':nud } ,'operator':op_symbols, 'end':{'lbp':0}, 'identifier':{'lbp':1, 'nud':nud}}

def paren(tokens):
    value = expression(tokens, 0)

    if tokens.current_token[1] != ")":
        tokens.error.append("Expecting closing parenthesis")

    return value


def expression(tokens, rbp=0):
    global op_symbols #, symbols
    
    t = tokens.current_token
    
    try:
        left = symbols[t[0]]['nud'](t)
    
        return traverse(tokens, left, rbp)    

    except KeyError:
        if tokens.current_token[1] == "-":
            tokens.current_token[1] = "-u"
            t = tokens.current_token

            tokens.read_next_token()

            try:
                right = symbols[tokens.current_token[0]]['nud'](tokens.current_token)
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
    global op_symbols

    tokens.read_next_token()    

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
        left = symbols[t[0]][t[1]]['led'](tokens, left, t) #TODO:passing the 't' into the function is a hack. when add() is called the current token has already advanced. must figure out a way to increment current token after add is called...or re-work the next/current token bit

        try:
            lbp = symbols[tokens.current_token[0]]['lbp']
        except KeyError:
            if tokens.current_token[1] == ")":
                return left
            else:
                lbp = symbols[tokens.current_token[0]][tokens.current_token[1]]['lbp']

    return left

def parse(t):

    token = Token(t)
    temp = expression(token)
    if token.error == []:
        return temp
    return token.error[0]

if __name__ == "__main__":
    t = [['identifier', 'x'], ['operator', '='], ['number', '3'], ['operator', '+'], ['number', '2'],['end', ';']]
    print parse(t)