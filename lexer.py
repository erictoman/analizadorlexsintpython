# Analizador lexico.
import ply.lex as lex
class Lexer:
    def __init__(self,tokens):
        #Tokens
        # Expresiones regulares para los tokens
        t_MAS    = r'\+'
        t_MENOS   = r'-'
        t_MULTIPLICADOR = r'\*'
        t_DIVISOR  = r'/'
        t_CORCHIZQ  = r'\['
        t_CORCHDER  = r'\]'
        t_FUNCION  = r"(grafica)"
        t_COMMA  = r"\,"
        t_IDRANGO  = r'[A-Z]'
        t_IDVALOR  = r'[a-z]'
        t_IGUAL = r'\='
        
        # Returno del valor
        def t_NUMERO(t):
            r'\d+'
            t.value = int(t.value)    
            return t

        # Saltos de linea
        def t_newline(t):
            r'\n+'
            t.lexer.lineno += len(t.value)
        
        # Ignora espacios y tabuladores
        t_ignore  = ' \t'

        # En caso de error
        def t_error(t):
            print("Caracter no reconocido '%s'" % t.value[0])
            t.lexer.skip(1)
            
        self.lexer = lex.lex()

    def analizar(self,texto):
        self.lexer.input(texto)
        st=""
        while True:
            tok = self.lexer.token()
            if not tok: 
                break      # No more input
            s = str(tok).replace("LexToken(","").split(",")
            st+="{0} -> {1}\n".format(s[0],s[1])
        return st

'''
analizadorLexico = Lexer(tokens)
data = A = [0, 15]
a = 2
grafica A + a
grafica A - a
grafica A * a
grafica A / a
#analizadorLexico.analizar(data)

lex=analizadorLexico.lexer
'''