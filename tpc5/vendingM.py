import json
from lex_vendingM import lexer

def save_stock(stock):
    out = []
    for it in stock:
        out.append({
            "cod": it["cod"],
            "nome": it["nome"],
            "quant": it["quant"],
            "preco": it["preco"]
        })
    with open("stock.json", "w", encoding="utf-8") as file:
        json.dump(out, file, indent=2)

def produto_existe(stock, cod):
    for p in stock:
        if p["cod"] == cod:
            return p
    return None

def processa(stock, saldo, line):
    lexer.input(line)
    tokens = list(lexer)
    if not tokens:
        return saldo

    # Identificar o comando principal (sair,selecionar,moeda...)
    comando = tokens[0].type

    if comando == "LISTAR":
        print("cod   | nome                      | quantidade | preço")
        print("-------------------------------------------------------")
        for p in stock:
            print(f"{p['cod']:5} | {p['nome'][:25]:25} | {p['quant']:10} | {p['preco']:.2f}")
    
    elif comando == "MOEDA":
        soma = 0
        for i, tok in enumerate(tokens):
            if tok.type == "NUM":
                valor = tok.value  # se token for do tipo numero extraimos o valor 
                next_tok = tokens[i+1].type if i+1 < len(tokens) else None #avançamos para o proximo token para saber euro|cent
                if next_tok == "EURO":
                    soma += int(valor)
                elif next_tok == "CENT":
                    soma += int(valor)*(0.01)
        saldo += soma
        print("maq: Saldo = ", saldo)
    
    elif comando == "SELECIONAR":
        cod = None
        for tok in tokens:
            if tok.type == "COD":
                cod = tok.value
                break
        if not cod:
            print("maq: Uso: SELECIONAR <código>") #Caso nao seja incluido o codigo a seguir a Selecionar print do uso do comando
            return saldo
        produto = produto_existe(stock, cod) #fun auxiliar que verifica existencia do produto e extrai nome
        if not produto:
            print("maq: Produto inexistente.")
            return saldo
        if produto["quant"] <= 0:
            print(f"maq: Produto '{produto['nome']}' esgotado.")
            return saldo
        preco = produto["preco"]
        if saldo < preco:
            print("maq: Saldo insufuciente para satisfazer o seu pedido")
            print(f"maq: Saldo = '{saldo}';Pedido = '{preco}'")
            return saldo
        produto["quant"] -= 1 #atualizamos a quantidade do produto depois de retirar
        saldo -= preco #atualizar o saldo restante do cliente
        print(f"maq: Pode retirar o produto dispensado \"{produto['nome']}\".")
        print("maq: Saldo =", saldo)
    
    elif comando == "SAIR":
        save_stock(stock)
        moedas_troco = {2:0,1:0,50:0,20:0,10:0,5:0}
        while saldo > 0:
            if saldo - 2 > 0:
                saldo = saldo - 2
                moedas_troco[2] += 1
            elif saldo - 1 > 0:
                saldo = saldo - 1
                moedas_troco[1] += 1
            elif saldo - 0.5 > 0:
                saldo = saldo - 0.5
                moedas_troco[50] += 1
            elif saldo - 0.2 > 0:
                saldo = saldo - 0.2
                moedas_troco[20] += 1
            elif saldo - 0.1 > 0:
                saldo = saldo - 0.1
                moedas_troco[10] += 1
            elif saldo - 0.05 > 0:
                saldo = saldo - 0.05
                moedas_troco[5] += 1
        exit(0)

    return saldo



def main():
    #dar load ao json do stock 
    with open("stock.json") as file:
        data = json.load(file)
    
    saldo_maq = 0

    print("maq: Stock carregado, Estado atualizado.")
    print("maq: Bom dia. Estou disponível para atender o seu pedido.")

    c = input(">> ")
    while c != "SAIR":
        saldo_maq = processa(data,saldo_maq,c)
        c = input(">> ")

    print("maq: Pode retirar o troco:")
    print("maq: Até à próxima!")
    

if __name__ == "__main__":
    main()
