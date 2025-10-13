
import sys
import re

def tokenize(input_string):
    reconhecidos = []
    mo = re.finditer(r'(?P<PREFIX>PREFIX)|(?P<SELECT>SELECT)|(?P<WHERE>WHERE)|(?P<FILTER>FILTER)|(?P<OPTIONAL>OPTIONAL)|(?P<UNION>UNION)|(?P<GRAPH>GRAPH)|(?P<ASK>ASK)|(?P<CONSTRUCT>CONSTRUCT)|(?P<DESCRIBE>DESCRIBE)|(?P<ORDERBY>ORDER\s+BY)|(?P<LIMIT>LIMIT)|(?P<OFFSET>OFFSET)|(?P<DISTINCT>DISTINCT)|(?P<REDUCED>REDUCED)|(?P<FROM>FROM)|(?P<NAMED>NAMED)|(?P<AS>AS)|(?P<IGUAL>=)|(?P<DIFERENTE>!=)|(?P<MENOR><)|(?P<MAIOR>>)|(?P<MENOR_IGUAL><=)|(?P<MAIOR_IGUAL>>=)|(?P<CA>\{)|(?P<CF>\})|(?P<PA>\()|(?P<PF>\))|(?P<PV>;)|(?P<VIRG>,)|(?P<PONTO>\.)|(?P<VARIAVEL>\?[A-Za-z_][A-Za-z0-9_]*)|(?P<NOME>"([^"\\]|\\.)*")|(?P<NUM>\d+(\.\d+)?)|(?P<IRI_ABREVIADO>[A-Za-z_][A-Za-z0-9_]*:[A-Za-z_][A-Za-z0-9_]*)|(?P<IDENTIFICADOR>[A-Za-z_][A-Za-z0-9_]*)|(?P<TAG_IDIOMA>@[a-zA-Z]+(-[a-zA-Z0-9]+)*)|(?P<SKIP>[ \t]+)|(?P<NEWLINE>\n)|(?P<ERRO>.)', input_string)
    for m in mo:
        dic = m.groupdict()
        if dic['PREFIX']:
            t = ("PREFIX", dic['PREFIX'], nlinha, m.span())

        elif dic['SELECT']:
            t = ("SELECT", dic['SELECT'], nlinha, m.span())
    
        elif dic['WHERE']:
            t = ("WHERE", dic['WHERE'], nlinha, m.span())
    
        elif dic['FILTER']:
            t = ("FILTER", dic['FILTER'], nlinha, m.span())
    
        elif dic['OPTIONAL']:
            t = ("OPTIONAL", dic['OPTIONAL'], nlinha, m.span())
    
        elif dic['UNION']:
            t = ("UNION", dic['UNION'], nlinha, m.span())
    
        elif dic['GRAPH']:
            t = ("GRAPH", dic['GRAPH'], nlinha, m.span())
    
        elif dic['ASK']:
            t = ("ASK", dic['ASK'], nlinha, m.span())
    
        elif dic['CONSTRUCT']:
            t = ("CONSTRUCT", dic['CONSTRUCT'], nlinha, m.span())
    
        elif dic['DESCRIBE']:
            t = ("DESCRIBE", dic['DESCRIBE'], nlinha, m.span())
    
        elif dic['ORDERBY']:
            t = ("ORDERBY", dic['ORDERBY'], nlinha, m.span())
    
        elif dic['LIMIT']:
            t = ("LIMIT", dic['LIMIT'], nlinha, m.span())
    
        elif dic['OFFSET']:
            t = ("OFFSET", dic['OFFSET'], nlinha, m.span())
    
        elif dic['DISTINCT']:
            t = ("DISTINCT", dic['DISTINCT'], nlinha, m.span())
    
        elif dic['REDUCED']:
            t = ("REDUCED", dic['REDUCED'], nlinha, m.span())
    
        elif dic['FROM']:
            t = ("FROM", dic['FROM'], nlinha, m.span())
    
        elif dic['NAMED']:
            t = ("NAMED", dic['NAMED'], nlinha, m.span())
    
        elif dic['AS']:
            t = ("AS", dic['AS'], nlinha, m.span())
    
        elif dic['IGUAL']:
            t = ("IGUAL", dic['IGUAL'], nlinha, m.span())
    
        elif dic['DIFERENTE']:
            t = ("DIFERENTE", dic['DIFERENTE'], nlinha, m.span())
    
        elif dic['MENOR']:
            t = ("MENOR", dic['MENOR'], nlinha, m.span())
    
        elif dic['MAIOR']:
            t = ("MAIOR", dic['MAIOR'], nlinha, m.span())
    
        elif dic['MENOR_IGUAL']:
            t = ("MENOR_IGUAL", dic['MENOR_IGUAL'], nlinha, m.span())
    
        elif dic['MAIOR_IGUAL']:
            t = ("MAIOR_IGUAL", dic['MAIOR_IGUAL'], nlinha, m.span())
    
        elif dic['CA']:
            t = ("CA", dic['CA'], nlinha, m.span())
    
        elif dic['CF']:
            t = ("CF", dic['CF'], nlinha, m.span())
    
        elif dic['PA']:
            t = ("PA", dic['PA'], nlinha, m.span())
    
        elif dic['PF']:
            t = ("PF", dic['PF'], nlinha, m.span())
    
        elif dic['PV']:
            t = ("PV", dic['PV'], nlinha, m.span())
    
        elif dic['VIRG']:
            t = ("VIRG", dic['VIRG'], nlinha, m.span())
    
        elif dic['PONTO']:
            t = ("PONTO", dic['PONTO'], nlinha, m.span())
    
        elif dic['VARIAVEL']:
            t = ("VARIAVEL", dic['VARIAVEL'], nlinha, m.span())
    
        elif dic['NOME']:
            t = ("NOME", dic['NOME'], nlinha, m.span())
    
        elif dic['NUM']:
            t = ("NUM", dic['NUM'], nlinha, m.span())
    
        elif dic['IRI_ABREVIADO']:
            t = ("IRI_ABREVIADO", dic['IRI_ABREVIADO'], nlinha, m.span())
    
        elif dic['IDENTIFICADOR']:
            t = ("IDENTIFICADOR", dic['IDENTIFICADOR'], nlinha, m.span())
    
        elif dic['TAG_IDIOMA']:
            t = ("TAG_IDIOMA", dic['TAG_IDIOMA'], nlinha, m.span())
    
        elif dic['SKIP']:
            t = ("SKIP", dic['SKIP'], nlinha, m.span())
    
        elif dic['NEWLINE']:
            t = ("NEWLINE", dic['NEWLINE'], nlinha, m.span())
    
        elif dic['ERRO']:
            t = ("ERRO", dic['ERRO'], nlinha, m.span())
    
        else:
            t = ("UNKNOWN", m.group(), nlinha, m.span())
        if not dic['SKIP'] and t[0] != 'UNKNOWN': reconhecidos.append(t)
    return reconhecidos

nlinha = 1
for linha in sys.stdin:
    for tok in tokenize(linha):
        print(tok) 
    nlinha += 1   

