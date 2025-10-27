from c_analex import lexer

prox_simb = ('Erro', '', 0, 0)

def parserError(simb):
    print(f"Erro sintático, token inesperado: {simb.type} ({simb.value})")

def rec_term(simb):
    global prox_simb
    if prox_simb and prox_simb.type == simb:
        print(f"Consumiu token: {simb} ({prox_simb.value})")
        prox_simb = lexer.token()
    else:
        parserError(prox_simb)

def rec_C():
    global prox_simb
    if prox_simb and prox_simb.type in ('MAIS', 'MENOS'):
        print(f"C → {prox_simb.type} A")
        simb = prox_simb.type
        rec_term(simb)
        rec_A()
    else:
        print("C → ε")

def rec_B():
    global prox_simb
    if prox_simb and prox_simb.type in ('VEZES', 'DIVIDIR'):
        print(f"B → {prox_simb.type} A")
        simb = prox_simb.type
        rec_term(simb)
        rec_A()
    else:
        print("B → C")
        rec_C()

def rec_A():
    global prox_simb
    if prox_simb and prox_simb.type in ('NUM', 'FLOAT'):
        print("A → Num B")
        rec_term(prox_simb.type)
        rec_B()

    elif prox_simb and prox_simb.type == 'PA':
        print("A → ( A )")
        rec_term('PA')
        rec_A()
        rec_term('PF')
        rec_B()

    elif prox_simb and prox_simb.type == 'MENOS':
        print("A → - Num B")
        rec_term('MENOS')
        if prox_simb and prox_simb.type in ('NUM', 'FLOAT'):
            rec_term(prox_simb.type)
            rec_B()
        else:
            parserError(prox_simb)
    else:
        parserError(prox_simb)

def rec_Parser(data):
    global prox_simb
    lexer.input(data)
    prox_simb = lexer.token()
    print("Início da análise sintática:")
    rec_A()
    print("Análise concluída!")
