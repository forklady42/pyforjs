counter = 0
tokens = ['(', 'number', '*', 'number', '+', 'number', ')', '*', '+']
current_token = tokens[0]



def read_next_token():
    global counter
    global current_token

    counter+=1
    if(counter<len(tokens)): 
        current_token = tokens[counter]

    print counter
    print current_token

def E():
    global current_token
    illegal =''
  

    if current_token == 'number':
        read_next_token()
        if current_token == '+':
            read_next_token()
            E()
        elif current_token == '-':
            read_next_token()
            E()
        elif current_token == '*':
            read_next_token()
            E()
        elif current_token == '/':
            read_next_token()
            E()
        elif current_token == '^':
            read_next_token()
            E()
        #elif current_token == ')':
         #   read_next_token()
        else:
            illegal = "ILLEGAL! Only the following characters can follow a number: +,*,/,^"
    elif current_token == 'number':
        read_next_token()
        if current_token == '-':
            read_next_token()
            E()
        elif current_token == '+':
            read_next_token()
            E()
        elif current_token == '*':
            read_next_token()
            E()
        elif current_token == '/':
            read_next_token()
            E()
        elif current_token == '^':
            read_next_token()
            E()
        else:
            illegal = "ILLEGAL! Only the following characters can follow a number: +,*,/,^"
    elif current_token == 'number':
        read_next_token()
        if current_token == '*':
            read_next_token()
            E()
        elif current_token == '-':
            read_next_token()
            E()
        elif current_token == '+':
            read_next_token()
            E()
        elif current_token == '/':
            read_next_token()
            E()
        elif current_token == '^':
            read_next_token()
            E()
        else:
            illegal = "ILLEGAL! Only the following characters can follow a number: +,*,/,^"
    elif current_token == 'number':
        read_next_token()
        if current_token == '/':
            read_next_token()
            E()
        elif current_token == '-':
            read_next_token()
            E()
        elif current_token == '*':
            read_next_token()
            E()
        elif current_token == '+':
            read_next_token()
            E()
        elif current_token == '^':
            read_next_token()
            E()
        else:
            illegal = "ILLEGAL! Only the following characters can follow a number: +,*,/,^"
    elif current_token == 'number':
        read_next_token()
        if current_token == '^':
            read_next_token()
            E()
        elif current_token == '-':
            read_next_token()
            E()
        elif current_token == '*':
            read_next_token()
            E()
        elif current_token == '/':
            read_next_token()
            E()
        elif current_token == '+':
            read_next_token()
            E()
        else:
            illegal = "ILLEGAL! Only the following characters can follow a number: +,*,/,^"
    elif current_token == 'number':
        read_next_token()
    elif current_token == '-':
        read_next_token()
        E()
    elif current_token == '(':
        read_next_token()
        E()
        #read_next_token()

        #print "in open, after call to E(), and after incrementing counter"
        #print counter

        if current_token == ')':
            print "here now"
            read_next_token()
            E()
        else:
            illegal = "ILLEGAL! Couldn't find closing parens!"
    else:
        illegal = "Encountered an illegal character. So I ended up here :/ Please start with anything but +,*,/,^."

    
    return illegal


print E()