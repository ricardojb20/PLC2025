Para a resolução deste TPC houve a necessidade de se criar um ficheiro .json que identificasse os tokens da linguangem SPARQL
[
    { 
        "id": "PREFIX",
        "expreg": "PREFIX" 
    },
    { 
        "id": "SELECT", 
        "expreg": "SELECT" 
    },
    { 
        "id": "WHERE", 
        "expreg": "WHERE" 
    },
    { 
        "id": "FILTER", 
        "expreg": "FILTER" 
    },
    { 
        "id": "OPTIONAL", 
        "expreg": "OPTIONAL" 
    },
    { 
        "id": "UNION", 
        "expreg": "UNION" 
    },
    { 
        "id": "GRAPH", 
        "expreg": "GRAPH" 
    },
    { 
        "id": "ASK", 
        "expreg": "ASK" 
    },
    { 
        "id": "CONSTRUCT", 
        "expreg": "CONSTRUCT" 
    },
    { 
        "id": "DESCRIBE", 
        "expreg": "DESCRIBE" 
    },
    { 
        "id": "ORDERBY", 
        "expreg": "ORDER\\s+BY" 
    },
    { 
        "id": "LIMIT", 
        "expreg": "LIMIT" 
    },
    { 
        "id": "OFFSET", 
        "expreg": "OFFSET" 
    },
    { 
        "id": "DISTINCT", 
        "expreg": "DISTINCT" 
    },
    { 
        "id": "REDUCED", 
        "expreg": "REDUCED" 
    },
    { 
        "id": "FROM", 
        "expreg": "FROM" 
    },
    { 
        "id": "NAMED", 
        "expreg": "NAMED" 
    },
    { 
        "id": "AS", 
        "expreg": "AS" 
    },
    { 
        "id": "IGUAL", 
        "expreg": "=" 
    },
    { 
        "id": "DIFERENTE", 
        "expreg": "!=" 
    },
    { 
        "id": "MENOR", 
        "expreg": "<" 
    },
    { 
        "id": "MAIOR", 
        "expreg": ">" 
    },
    { 
        "id": "MENOR_IGUAL", 
        "expreg": "<=" 
    },
    { 
        "id": "MAIOR_IGUAL", 
        "expreg": ">=" 
    },
    { 
        "id": "CA", 
        "expreg": "\\{" 
    },
    { 
        "id": "CF", 
        "expreg": "\\}" 
    },
    { 
        "id": "PA", 
        "expreg": "\\(" 
    },
    { 
        "id": "PF", 
        "expreg": "\\)" 
    },
    { 
        "id": "PV", 
        "expreg": ";" 
    },
    { 
        "id": "VIRG", 
        "expreg": "," 
    },
    { 
        "id": "PONTO", 
        "expreg": "\\." 
    },
    { 
        "id": "VARIAVEL", 
        "expreg": "\\?[A-Za-z_][A-Za-z0-9_]*" 
    },
    { 
        "id": "NOME", 
        "expreg": "\"([^\"\\\\]|\\\\.)*\"" 
    },
    { 
        "id": "NUM", 
        "expreg": "\\d+(\\.\\d+)?" 
    },
    { 
        "id": "IRI_ABREVIADO", 
        "expreg": "[A-Za-z_][A-Za-z0-9_]*:[A-Za-z_][A-Za-z0-9_]*" 
    },
    { 
        "id": "IDENTIFICADOR", 
        "expreg": "[A-Za-z_][A-Za-z0-9_]*" 
    },
    { 
        "id": "TAG_IDIOMA", 
        "expreg": "@[a-zA-Z]+(-[a-zA-Z0-9]+)*" 
    },
    { 
        "id": "SKIP", 
        "expreg": "[ \\t]+" 
    },
    { 
        "id": "NEWLINE", 
        "expreg": "\\n" 
    },
    { 
        "id": "ERRO",  
        "expreg": "." 
    }
]
    

Após criar o ficheiro basta usa-lo como input do programa get_tokenizer2.py para ser gerado um novo ficheiro .py com o codigo do analisador lexico da linguagem
(python gen_tokenizer.py tpc4_TOKENS_SPARQL.json > tpc4_LEXICO_SPARQL.py)
A partir daí ja temos um analisador pronto a ser usado. 
EXEMPLO dado no encunciado do TPC:
select ?nome ?desc where {
('IDENTIFICADOR', 'select', 1, (0, 6))
('VARIAVEL', '?nome', 1, (7, 12))
('VARIAVEL', '?desc', 1, (13, 18))
('IDENTIFICADOR', 'where', 1, (19, 24))
('CA', '{', 1, (25, 26))
('NEWLINE', '\n', 1, (26, 27))

?s a dbo:MusicalArtist.
('VARIAVEL', '?s', 2, (0, 2))
('IDENTIFICADOR', 'a', 2, (3, 4))
('IRI_ABREVIADO', 'dbo:MusicalArtist', 2, (5, 22))
('PONTO', '.', 2, (22, 23))
('NEWLINE', '\n', 2, (23, 24))

?s foaf:name "Chuck Berry"@en .
('VARIAVEL', '?s', 3, (0, 2))
('IRI_ABREVIADO', 'foaf:name', 3, (3, 12))
('NOME', '"Chuck Berry"', 3, (13, 26))
('TAG_IDIOMA', '@en', 3, (26, 29))
('PONTO', '.', 3, (30, 31))
('NEWLINE', '\n', 3, (31, 32))

?w dbo:artist ?s.
('VARIAVEL', '?w', 4, (0, 2))
('IRI_ABREVIADO', 'dbo:artist', 4, (3, 13))
('VARIAVEL', '?s', 4, (14, 16))
('PONTO', '.', 4, (16, 17))
('NEWLINE', '\n', 4, (17, 18))

?w foaf:name ?nome.
('VARIAVEL', '?w', 5, (0, 2))
('IRI_ABREVIADO', 'foaf:name', 5, (3, 12))
('VARIAVEL', '?nome', 5, (13, 18))
('PONTO', '.', 5, (18, 19))
('NEWLINE', '\n', 5, (19, 20))

?w dbo:abstract ?desc
('VARIAVEL', '?w', 6, (0, 2))
('IRI_ABREVIADO', 'dbo:abstract', 6, (3, 15))
('VARIAVEL', '?desc', 6, (16, 21))
('NEWLINE', '\n', 6, (21, 22))

} LIMIT 1000
('CF', '}', 7, (0, 1))
('LIMIT', 'LIMIT', 7, (2, 7))
('NUM', '1000', 7, (8, 12))
('NEWLINE', '\n', 7, (12, 13))
