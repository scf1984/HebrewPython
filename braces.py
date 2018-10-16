# iterate on characters from string
    # find opening braces and "remember" them in order
    # find closing braces and make sure it fits the last opening braces
        # if yes, "forget" last opening braces
        # if no, return False
# if memory of opening braces is not empty - return false
# else return True

def check_braces(text):
    braces = []
    for c in text:
        if c in '({[':
            braces.append(c)
        if c in ')}]':
            try:
                b = braces.pop()
            except IndexError:
                return False
            if b == '(' and c == ')':
                continue
            if b == '{' and c == '}':
                continue
            if b == '[' and c == ']':
                continue
            return False
    if braces:
        return False
    else:
        return True

print(check_braces('()'))
print(check_braces('[({})]'))
print(check_braces(',]'))
print(check_braces('(kjgsd'))
print(check_braces('(kjgsd))'))
print(check_braces('(]'))
