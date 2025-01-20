x = "{(})"
for i in range(len(x)):
    if x[i] == '(':
        if ((x[-(i+1)] == ')') or (x[i+1] == ')')):
            res = True
        else:
            res = False
            break 
    elif(x[i] == '{'):
        if ((x[-(i+1)] == '}') or (x[i+1] == '}')):
            res = True
        else:
            res = False
            break 
    elif(x[i] == '['):
        if ((x[-(i+1)] == ']') or (x[i+1] == ']')):
            res = True
        else:
            res = False
            break 
res
