def load_curriculo(curriculo):
    """ 
    Carrega os currículos por ano e retorna o html
    """
    html_include = ""
    ano = ""
    if curriculo:
        for item in curriculo:
            ano_aux = item.data.strftime("%Y")
            mes = item.data.strftime("%B")

            if ano != ano_aux:
                html_include += f"<p class='text1'><text class='text3'> { ano_aux }:</text></p>"
            
            html_include += f"<p class='text1'>&bull; { mes } - { item.descricao } </p>"
            ano = ano_aux 
    else:
        html_include += "<p class='text2' style='font-weight: bold;'>Nenhum Resultado</p>"
    return html_include

def load_premios(premios):
    """ 
    Carrega os prêmios por evento e retorna o html
    """
    html_include = ""
    evento = ""

    if premios:
        for premio in premios:

            if premio.evento != evento:
                html_include += f"<br><p class='text1'><text class='text3'> { premio.evento } - Espetáculo { premio.espetaculo } </text></p>"
            
            html_include += f"<p class='text1'>&bull; { premio.premio }</p>"
            evento = premio.evento
    else:
        html_include += "<p class='text2' style='font-weight: bold;'>Nenhum Resultado</p>"
    
    return html_include