next = -1
tokens = ['(', 'number', '+', 'number', ')', '*', '+']



def reset(save):
    next = save

def E():
    global next
    save = next
    next+=1
    
    
    if E1():
        print 'E1 returned True':
        return True
    else:
        reset(save)
    if E2():
        print 'E2 returned True'
        return True
    else:
        reset(save)
    if E3():
        print 'E3 returned True'
        return True
    else:
        reset(save)
    if E4():
        print 'E4 returned True'
        return True
    else:
        reset(save)
    if E5():
        print 'E5 returned True'
        return True
    else:
        reset(save)
    if E6():
        print 'E6 returned True'
        return True
    else:
        reset(save)
    if E7():
        print 'E7 returned True'
        return True
    else:
        reset(save)
    if E8():
        print 'E8 returned True'
        return True
    else:
        reset(save)
    return False
    

def E1():
    global next
    if tokens[next] == "number":
        next+=1
        return True
    else:
        print "E1 False"
        return False

def E2():
    global next
    if tokens[next] == '(':
        next+=1
        if E():
            if tokens[next] == ')':
                next+=1
                return True
            else:
                print "E2 False #1"
                return False
        else:
            print "E2 False #2"
            return False
        
    else:
        print "E2 False #3"
        return False

def E3():
    global next
    if tokens[next] == "number":
        next+=1
        if tokens[next] == '+':
            next+=1
            if E():
                return True
            else:
                print "E3 False #1"
                return False
        else:
            print "E3 False #2"
            return False
    else:
        print "E3 False #3"
        return False

def E4():
    global next
    if tokens[next] == "number":
        next+=1
        if tokens[next] == '*':
            next+=1
            if E():
                return True
            else:
                print "E4 False #1"
                return False
        else:
            print "E4 False #2"
            return False
    else:
        print "E4 False #3"
        return False

def E5():
    global next
    if tokens[next] == "number":
        next+=1
        if tokens[next] == '/':
            next+=1
            if E():
                return True
            else:
                print "E5 False #1"
                return False
        else:
            print "E5 False #2"
            return False
    else:
        print "E5 False #3"
        return False

def E6():
    global next
    if tokens[next] == "number":
        next+=1
        if tokens[next] == '^':
            next+=1
            if E():
                return True
            else:
                print "E6 False #1"
                return False
        else:
            print "E6 False #2"
            return False
    else:
        print "E6 False #2"
        return False

def E7():
    global next
    if tokens[next] == "number":
        next+=1
        if tokens[next] == '-':
            next+=1
            if E():
                return True
            else:
                print "E7 False #1"
                return False
        else:
            print "E7 False #2"
            return False
    else:
        print "E7 False #3"
        return False

def E8():
    global next
    if tokens[next] == "-":
        next+=1
        if E():
            return True
        else:
            print "E8 False #1"
            return False
    else:
        print "E8 False #2"
        return False
        
        
while next < len(tokens):        
    sprint E()