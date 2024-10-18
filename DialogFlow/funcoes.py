def criarMessengerCard():
    return {
        "type":"info",
        "title":"",
        "subtitle":"",
        "image": {
            "src" : {
                "rawUrl":""
            }
        },
        "actionLink":""
    }
    
def criarCustomCard():
    return {
        "card": {
            "title":"",
            "subtitle":"",
            "imageUri":"",
            "buttons": [
                {
                    "text":"botão",
                    "postback":""
                }
            ]
        }
    }
    
def obterCardsServicos(tipoCard = 'messenger'):
    listaCards = []
    from Model.Servico import Servico
    servicos = Servico(0,"",0).consultar()
    cartao = None
    for servico in servicos:
        if tipoCard == 'messenger':
            cartao = criarMessengerCard()
            cartao['title'] = servico.nome
            cartao['subtitlesubtitle'] = f"Serviço: {servico.nome} | R$ {servico.preco}"
            cartao['image']['src']['rawUrl'] =""
            cartao['actionLink'] = ""
            
        elif tipoCard == 'custom':
            cartao = criarCustomCard()
            cartao['card']['title'] = servico.nome
            cartao['card']['subtitle'] = f"Serviço: {servico.nome} | R$ {servico.preco}"
            cartao['card']['imageUri'] = ""
            cartao['card']['buttons'][0]['text'] = "Clique aqui para mais informações";
            cartao['card']['buttons'][0]['postback'] = ""
            
        listaCards.append(cartao)
    return listaCards
    
