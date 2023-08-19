listaDeCondicoes = [
    {
        "Dia": "D1",
        "Clima": "Sol",
        "Temperatura": "Quente",
        "Umidade": "Alta",
        "Vento": "Fraco"
    },
    {
        "Dia": "D2",
        "Clima": "Sol",
        "Temperatura": "Quente",
        "Umidade": "Alta",
        "Vento": "Forte"
    },
    {
        "Dia": "D3",
        "Clima": "Nublado",
        "Temperatura": "Quente",
        "Umidade": "Alta",
        "Vento": "Fraco"
    },
    {
        "Dia": "D4",
        "Clima": "Chuva",
        "Temperatura": "Médio",
        "Umidade": "Alta",
        "Vento": "Fraco"
    },
    {
        "Dia": "D5",
        "Clima": "Chuva",
        "Temperatura": "Frio",
        "Umidade": "Normal",
        "Vento": "Fraco"
    },
    {
        "Dia": "D6",
        "Clima": "Chuva",
        "Temperatura": "Frio",
        "Umidade": "Normal",
        "Vento": "Forte"
    },
    {
        "Dia": "D7",
        "Clima": "Nublado",
        "Temperatura": "Frio",
        "Umidade": "Normal",
        "Vento": "Forte"
    },
    {
        "Dia": "D8",
        "Clima": "Sol",
        "Temperatura": "Médio",
        "Umidade": "Alta",
        "Vento": "Fraco"
    }
]


def playTennisOrNot():
    for i in listaDeCondicoes:
        if i['Clima'] == "Sol" or i['Clima'] == "Chuva" and i['Vento'] == "Forte":
            i['PlayTennis'] = "Não"
        else:
            i['PlayTennis'] = "Sim"
        print("\n", i)


playTennisOrNot()
