start_ -> PROGRAM IDENTIFICADOR ; declaracoes BEGIN bloco_comandos END .

declaracoes -> declaracoes declaracao_tipo
    | ε

declaracao_tipo -> dec_variaveis
    | dec_funcao

dec_variaveis -> VAR lista_vars

lista_vars -> lista_vars lista_ids : tipo_variaveis ;
    | ε

lista_ids -> IDENTIFICADOR
    | lista_ids , IDENTIFICADOR

tipo_variaveis -> INTEGER_TYPE
    | REAL_TYPE
    | BOOLEAN_TYPE
    | CHAR_TYPE
    | STRING_TYPE
    | ARRAY [ INTEGER .. INTEGER ] OF tipo_variaveis

dec_funcao -> FUNCTION IDENTIFICADOR ( parametros ) : tipo_variaveis ; dec_variaveis_f BEGIN bloco_comandos_f END ;

parametros -> parametro
    | parametro ; parametros
    | ε

parametro -> parametro lista_ids : tipo_variaveis
    | ε

bloco_comandos -> lista_comandos_pv comando
    | lista_comandos_pv
    | comando
    | ε

lista_comandos_pv -> comando_pv
    | lista_comandos_pv comando_pv

comando_pv -> comando ;

comando -> atribuicao
    | leitura
    | escrita
    | if_h
    | while_h
    | for_h
    | return
    | BEGIN bloco_comandos END

atribuicao -> IDENTIFICADOR := expressao
    | IDENTIFICADOR := chamada_funcao

leitura -> READLN ( IDENTIFICADOR )
    | READLN ( IDENTIFICADOR [ expressao ] )

escrita -> WRITELN ( argumentos_escrita )

argumentos_escrita -> argumento
    | argumentos_escrita , argumento
    | ε

argumento -> STRING
    | IDENTIFICADOR
    | IDENTIFICADOR [ expressao ]

if_h -> IF expressao THEN comando
    | IF expressao THEN comando ELSE comando

while_h -> WHILE expressao DO comando

for_h -> FOR IDENTIFICADOR := expressao TO expressao DO comando
    | FOR IDENTIFICADOR := expressao DOWNTO expressao DO comando

chamada_funcao -> IDENTIFICADOR ( lista_ids )
    | IDENTIFICADOR ( )

expressao -> expressao + expressao
    | expressao - expressao
    | expressao * expressao
    | expressao / expressao
    | expressao DIV expressao
    | expressao MOD expressao
    | expressao AND expressao
    | expressao OR expressao
    | expressao = expressao
    | expressao <> expressao
    | expressao < expressao
    | expressao > expressao
    | expressao <= expressao
    | expressao >= expressao
    | NOT expressao
    | ( expressao )
    | IDENTIFICADOR
    | IDENTIFICADOR [ expressao ]
    | INTEGER
    | REAL
    | STRING
    | TRUE
    | FALSE
    | LENGTH ( IDENTIFICADOR )

return -> IDENTIFICADOR := IDENTIFICADOR ;
