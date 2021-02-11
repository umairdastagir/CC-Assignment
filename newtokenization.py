import re
def check(k):
    for i in k:
        if i in Reserve['Operators']:
            return False
        elif i in Reserve['AssignmentOperators']:
            return False
        elif i in Reserve['Comperision']:
            return False
        elif i in Reserve['LeftShift']:
            return False
        elif i in Reserve['RightShift']:
            return False
        elif i in Reserve['LeftParen']:
            return False
        elif i in Reserve['RightParen']:
            return False
        elif i in ['#','@','%','&']:
            return False

    return True

Reserve= dict(
    Operators=['+', '-', '*', '/', '%'],
    AssignmentOperators='=',
    keyword=['if', 'else', 'switch', 'for', 'while', 'do', 'void', 'cin', 'cout',"int", 'float','main','str', 'double','return'],
    brackets=['{', '}'],
    LeftParen='(',
    RightParen=')',
    Comperision=['>','<','==','<=','>='],
    Terminator=';',
    LeftShift='<<',
    RightShift='>>'
              )

string=""
with open("C:\Users\Syed Umair\Desktop\new.txt" ,'r') as readfile:
    print(readfile.readline())
    for i in readfile.readlines():
        for j in i.split():
            if j in Reserve['Operators']:
                string+='<Operator,'+j+"  >\n"
            elif j in Reserve['AssignmentOperators']:
                string+='<AssignmentOpe,'+j+"  >\n"
            elif j in Reserve['keyword']:
                string+='<keyword,'+j+"  >\n"
            elif j in Reserve['brackets']:
                string += '<curlyBracket,' + j + ">\n"
            elif j in Reserve['LeftParen']:
                string += '<LeftParen,' + j + "  >\n"
            elif j in Reserve['RightParen']:
                string += '<RightParen,' + j + "  >\n"
            elif j in Reserve['Comperision']:
                string += '<comperisionOpe,' + j + "  >\n"
            elif j in Reserve['Terminator']:
                string += '<Terminator,' + j + "  >\n"
            elif j in Reserve['LeftShift']:
                string += '<leftshift,' + j + "  >\n"
            elif j in Reserve['RightShift']:
                string += '<Rightshift,' + j + "  >\n"
            else:
                if re.findall('[a-zA-Z]',j):
                    if re.findall('[a-zA-Z]',j[0]) and check(j) and re.findall('[a-zA-Z]',j[0]) or j[0]=='_':
                        string += '<Identifiers,' + j + "  >\n"
                    else:
                        print("Invalid Tokens\t", j)
                        exit()

                elif re.findall('[0-9]',j) and check(j):
                    if j[-1]==";" or re.findall('[a-zA-z]',j[-1]) or j[-1]=='=':
                        print("Invalid Token"+j)
                        exit()
                    string += '<Number,' + j + "  >\n"
                else:
                    print(j)
                    print("Invalid Tokens\t",j)
                    exit()
with open("new2.txt","w") as writer:
    writer.write(string)
