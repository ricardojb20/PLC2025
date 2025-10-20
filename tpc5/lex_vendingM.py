import ply.lex as lex

# Lista de tokens
tokens = (
    'MOEDA',
    'SELECIONAR',
    'LISTAR',
    'SAIR',
    'NUM',
    'EURO',
    'CENT',
    'COD',
    'VIRG',
    'PONTO'
)

# Tokens simples
t_VIRG = r','
t_PONTO = r'\.'

# Palavras reservadas
def t_MOEDA(t):
    r'MOEDA'
    return t

def t_SELECIONAR(t):
    r'SELECIONAR'
    return t

def t_LISTAR(t):
    r'LISTAR'
    return t

def t_SAIR(t):
    r'SAIR'
    return t

# Número (inteiro)
def t_NUM(t):
    r'\d+'
    return t

# Unidades monetárias
def t_EURO(t):
    r'e'
    return t

def t_CENT(t):
    r'c'
    return t

# Código de produto (ex: A23)
def t_COD(t):
    r'[A]\d{2}'
    return t

# Ignorar espaços e tabs
t_ignore = ' \t'

# Nova linha
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Erros léxicos
def t_error(t):
    print(f"Caractere inválido: '{t.value[0]}'")
    t.lexer.skip(1)

# Construir o lexer
lexer = lex.lex()
