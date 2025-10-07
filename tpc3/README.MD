import re

def markdown_to_html(markdown):
    html = ""
    lines = markdown.split("\n")
    in_list = False  

    for line in lines:
        line = line.strip()

        # Cabeçalhos: linhas iniciadas por "# texto", ou "## texto" ou "### texto"
        if re.match(r"^### (.*)", line):
            html += f"<h3>{re.findall(r'^### (.*)', line)[0]}</h3>\n"
        elif re.match(r"^## (.*)", line):
            html += f"<h2>{re.findall(r'^## (.*)', line)[0]}</h2>\n"
        elif re.match(r"^# (.*)", line):
            html += f"<h1>{re.findall(r'^# (.*)', line)[0]}</h1>\n"

        # caso de lista numerada
        elif re.match(r"^\d+\. (.*)", line):
            if not in_list:
                html += "<ol>\n"
                in_list = True
            item = re.findall(r"^\d+\. (.*)", line)[0]
            html += f"<li>{item}</li>\n"
        else:
            # Fechar lista se já estava aberta
            if in_list:
                html += "</ol>\n"
                in_list = False
            # Caso contrário apenas texto normal
            html += line + "\n"

    # Fechar a lista no fim do texto se ainda estiver aberta
    if in_list:
        html += "</ol>\n"

    # --- Substituições de forataçao ---
    # Bold: pedaços de texto entre "**":
    html = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", html)
    # Itálico: pedaços de texto entre "*":
    html = re.sub(r"\*(.*?)\*", r"<i>\1</i>", html)
    # Link: [texto](endereço URL)
    html = re.sub(r"\[(.*?)\]\((.*?)\)", r'<a href="\2">\1</a>', html)
    # Imagem: ![texto alternativo](path para a imagem)
    html = re.sub(r"!\[(.*?)\]\((.*?)\)", r'<img src="\2" alt="\1"/>', html)

    return html.strip() #remover espaços vazios
