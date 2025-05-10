# Avaliar praias da região
# entrada 
# processamento
# saida

class Praia:

    def __init__(self, nome, distancia_centro, num_medio_veranistas, tipo_acesso):

        self.nome = nome
        self.distancia_centro = distancia_centro
        self.num_medio_veranistas = num_medio_veranistas
        self.tipo_acesso = tipo_acesso


# programa principal
# informar as praias
praias = {}
continua = True

while continua:
    nome_praia = input("Informe o nome da praia")
    distancia_centro = float(input("Informe a distância em KM da praia ao centro de sua cidade"))
    media_veranistas = int(input("Informe a quantidade média de veranistas da última temporada"))
    tipo_acesso_praia = int(input("Informe o tipo de acesso à praia (0 - acesso não asfaltado OU 1 - acesso asfaltado)"))

    praia = Praia(nome_praia, distancia_centro, media_veranistas, tipo_acesso_praia)

    # valida a resposta (S ou N)
    continua_reposta = True
    while continua_reposta
    resposta = input("Deseja informar uma nova praia ('S'im ou 'N'ão)")
    if resposta.upper().startswith('s') or resposta.upper().startswith('s')
    resposta.upper() = 'N':
        continua = False
   




