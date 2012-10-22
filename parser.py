"""parse_tree_result = {
'type': "+",
'left': {'type': "number", 'value': 12 },
'right': {'type': "/", 'left': {'type': "number", 'value': 4 },'right': {'type': "number", 'value': 6 }}
}"""

#tokens = [['number', 12], ['operator', '+'], ['number', 4], ['operator', '/'], ['number', 6]]
tokens = [['number', 12], ['operator', '/'], ['number', 4], ['operator', '+'], ['number', 6]]

#tokens = [['number', 12], ['operator', '+'], ['number', 4]]

counter = 0
current_token = tokens[0]

def nud(l=''): #this empty string argument was a work around b/c when current token is number. the function that should be called is nud, but the algorithm doesn't seem to consider condidition within while loop?
    left = {'type':current_token[0], 'value':current_token[1]}
    return left

def add(l, t):
    tree = {'type':t[1], 'left': l, 'right': expression(10)}
    return tree

def div(l, t):
    tree = {'type':t[1], 'left': l, 'right': expression(20)}
    return tree

def mul(l, t):
    tree = {'type':t[1], 'left': l, 'right': expression(20)}
    return tree

#lambda x: x + n
op_symbols = {'+': {'lbp':10, 'led':add}, '/':{'lbp':20, 'led':div}, '*':{'lbp':20, 'led':mul}}
symbols = {'number':{'lbp':1, 'nud': nud, 'led':nud } ,'operator':op_symbols, 'end':{'lbp':0}}

def read_next_token():
    global counter, current_token

    counter+=1

    if counter < len(tokens):
        current_token = tokens[counter]
    else:
        current_token = ['end', 0]

def expression(rbp=0):
    global current_token, op_symbols #, symbols
    
    t = current_token
    
    left = symbols[t[0]]['nud']() #TODO: add error handling for the instance where the first token isn't a number...or something invalid.
    read_next_token()
    

    try:
        lbp = symbols[current_token[0]]['lbp']
    except KeyError:
        lbp = symbols[current_token[0]][current_token[1]]['lbp']

    while rbp < lbp:
        t = current_token
        read_next_token()
        left = symbols[t[0]][t[1]]['led'](left, t) #TODO:passing the 't' into the function is a hack. when add() is called the current token has already advanced. must figure out a way to increment current token after add is called...or re-work the next/current token bit

        try:
            lbp = symbols[current_token[0]]['lbp']
        except KeyError:
            lbp = symbols[current_token[0]][current_token[1]]['lbp']

    return left

def parse():
    return expression()


print parse()



