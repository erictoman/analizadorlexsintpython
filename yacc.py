import numpy as np
from ply import lex
from matplotlib.pyplot import *
class Yacc():
    def __init__(self,tokens,lex):
        #Diccionario de variables
        names = {}
        vals = {}

        def p_statement_assign(p):
            '''statement : IDRANGO IGUAL expression
                        | IDVALOR IGUAL NUMERO'''
            if p[1].isupper(): names[p[1]]=p[3]
            elif p[1].islower(): vals[p[1]]=p[3]
            

        def p_statement_expr(p):
            'statement : expression'
            print(p[1])

        def p_expression_binop(p):
            '''expression : FUNCION expression MAS expression
                        | FUNCION expression MENOS expression
                        | FUNCION expression MULTIPLICADOR expression
                        | FUNCION expression DIVISOR expression'''
            def f(x):
                return x
            if p[3] == '+'  : 
                x=p[2]
                plot(x,[f(i)+p[4] for i in x])
                show()
            elif p[3] == '-': 
                x=p[2]
                plot(x,[f(i)-p[4] for i in x])
                show()
            elif p[3] == '*': 
                x=p[2]
                plot(x,[f(i)*p[4] for i in x])
                show()
            elif p[3] == '/': 
                x=p[2]
                plot(x,[f(i)/p[4] for i in x])
                show()
        
        def p_expression_binopS(p):
            '''expression : FUNCION expression MAS NUMERO
                        | FUNCION expression MENOS NUMERO
                        | FUNCION expression MULTIPLICADOR NUMERO
                        | FUNCION expression DIVISOR NUMERO'''
            def f(x):
                return x
            if p[3] == '+'  : 
                x=p[2]
                plot(x,[f(i)+p[4] for i in x])
                show()
            elif p[3] == '-': 
                x=p[2]
                plot(x,[f(i)-p[4] for i in x])
                show()
            elif p[3] == '*': 
                x=p[2]
                plot(x,[f(i)*p[4] for i in x])
                show()
            elif p[3] == '/': 
                x=p[2]
                plot(x,[f(i)/p[4] for i in x])
                show()

        def p_expression_group(p):
            'expression : CORCHIZQ NUMERO COMMA NUMERO CORCHDER'
            p[0] = np.array([p[2],p[4]])

        def p_expression_name(p):
            'expression : NUMERO'
            p[0]=p[1]

        def p_expression_name(p):
            'expression : IDRANGO'
            try:
                p[0] = names[p[1]]
            except LookupError:
                print(f"Undefined name {p[1]!r}")
                p[0] = 0

       
        def p_expression_nameV(p):
            'expression : IDVALOR'
            try:
                p[0] = vals[p[1]]
            except LookupError:
                print(f"Undefined name {p[1]!r}")
                p[0] = 0

        def p_error(p):
            print(f"Syntax error at {p.value!r}")

        import ply.yacc as yacc
        self.yacc=yacc.yacc()

    def Parse(self,text):
        self.yacc.parse(text)