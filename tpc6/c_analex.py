import ply.lex as lex

tokens = ('MAIS','MENOS','VEZES','DIVIDIR','PA','PF','NUM','FLOAT')

t_MAIS    = r'\+'
t_MENOS   = r'-'
t_VEZES   = r'\*'
t_DIVIDIR = r'/'
t_PA      = r'\('
t_PF      = r'\)'

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Caractere ilegal: '{t.value[0]}' na linha {t.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()

