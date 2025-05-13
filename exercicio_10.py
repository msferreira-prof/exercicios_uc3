# Avaliar praias da região
# entrada 
# processamento
# saida

# classe Praia - caracteristicas da praia
class Praia:
    def __init__(self, nome, distancia_centro, media_veranistas, tipo_acesso):
        self.nome = nome
        self.distancia_centro = distancia_centro
        self.media_veranistas = media_veranistas
        self.tipo_acesso = tipo_acesso


def obter_praias():
    praias = []
    continua = True

    while continua:
        nome_praia = input("Informe o nome da praia: ")
        distancia_centro = float(input("Informe a distância em KM da praia ao centro de sua cidade: "))
        media_veranistas = int(input("Informe a quantidade média de veranistas da última temporada: "))
        tipo_acesso_praia = int(input("Informe o tipo de acesso à praia (0 - acesso não asfaltado OU 1 - acesso asfaltado): "))

        praia = Praia(nome_praia, distancia_centro, media_veranistas, tipo_acesso_praia)
        praias.append(praia)

        # valida a resposta (S ou N)
        continua_reposta = True
        while continua_reposta:
            resposta = input("Digite (S)im para nova praia ou (N)ão para sair: ")
            if len(resposta) > 1 or not (resposta.upper().startswith('S') or resposta.upper().startswith('N')):
                print("Responda novamente, por favor! Digite (S)im ou (N)ão: ")
            elif resposta.upper().startswith('N'):
                continua_reposta = False
                continua = False
            else:
                continua_reposta = False

    return praias


# funcao para contar praias que distam mais de 15km do centro
def calcular_praias_15km(lista_praias):
    numero_praias = 0

    for praia in lista_praias:
        if praia.distancia_centro > 15:
            numero_praias = numero_praias + 1
    
    return numero_praias


# funcao para calcular a qtd media de veranistas para praias não asfaltadas
def calcular_media_veranistas(lista_praias):
    media_veranistas_praias = 0
    qtd_veranistas = 0
    qtd_praias = 0

    for praia in lista_praias:
        if praia.tipo_acesso == 0:
            qtd_praias += 1
            qtd_veranistas = qtd_veranistas + praia.media_veranistas
    
    if qtd_praias > 0:
        media_veranistas_praias = qtd_veranistas / qtd_praias
    
    return media_veranistas_praias


# funcao para recuperar o nome e a distancia do centro de praias asfaltadas com menos de 1000 veranistas
def recuperar_praias_asfaltadas_menos_1000_veranistas(lista_praias):
    praias_asfaltadas = []
    for praia in lista_praias:
        if praia.tipo_acesso == 1 and praia.media_veranistas < 1000:
            praia_selecionada = {"nome": praia.nome, "distancia_centro": praia.distancia_centro}
            praias_asfaltadas.append(praia_selecionada)
    
    return praias_asfaltadas


def exibir_praias(cabecalho, lista_praias):
    print()
    print(cabecalho)
    print('-'*len(cabecalho))
    
    for praia in lista_praias:
        print("Praia: ", praia["nome"], " -> ", f'Distância: {praia["distancia_centro"]:02d}', 'Km')
    
    print()


# programa principal
# informar as praias
praias = []
praias = obter_praias()

# processa a letra a
numero_praias_15km = calcular_praias_15km(praias)

# processa a letra b
media_veranistas_praias_nao_asfaltadas = calcular_media_veranistas(praias)

# processa a letra c
praias_asfaltadas = recuperar_praias_asfaltadas_menos_1000_veranistas(praias)

# imprimir resultados
print()
print(f"Número de praias que distam mais de 15km do centro: {numero_praias_15km:03d}")
print(f"Quantidade média de veranistas para praias não asfaltadas: {media_veranistas_praias_nao_asfaltadas:.2f} veranistas")
exibir_praias("Praias asfaltadas com menos de 1000 veranistas:", praias_asfaltadas)