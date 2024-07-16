
# Abrir o arquivo

arquivo = open("dados.txt") #abrindo como leitura
# conteudo1 = (arquivo.read()) # retorna o conteúdo em string
# conteudo2 = arquivo.readlines() # retorna o conteúdo em lista 
# print(conteudo1) # um deles tem que estar comentado, pois não é possível ler 2x
# print(conteudo2)

linhas = []
for linha in arquivo:
    linhas.append(linha.strip().upper())

print(linhas)

arquivo.close()

# bloco with - criar contexto de algo

with open("dados.txt") as arquivo2:
    #arquivo2.write('teste')
    conteudo = arquivo2.read()
    print(conteudo)

print("teste teste")





#----------------------------------------
# Escrever no arquivo
# w - substitui todo o arquivo

# with open("dados.txt", "w") as arquivo3: #abrindo para escrever
#     arquivo3.write("Fruta tropical")


#----------------------------------------
# Adicionar linha no arquivo
# a - adiciona linha no arquivo (a = append)

#with open("dados.txt", "a") as arquivo4: #abrindo para escrever
    #arquivo4.write("\nFruta afrodisiaca")




#ler arquivo produtos.csv e 
#carregar em memória uma lista em que cada produto é um dict
print("-------------------------------------------------------")
def linha_para_produto(linha):
    dados = (linha.strip().split(','))
    return{
            "nome" : dados[0],
            "descricao" : dados[1],
            "preco" : float(dados[2]),
            "imagem" : dados[3]
    }

def obter_produtos():

    with open("produtos.csv") as arquivo_produtos:
        produtos = []
        for linha in arquivo_produtos:
            produto = linha_para_produto(linha)
            produtos.append(produto) #lista de dicionários
        return produtos



def salvar_produto(nome, descricao, preco, imagem):
    texto = f"\n{nome},{descricao},{preco},{imagem}"
    with open("produtos.csv", "a") as arquivo_podutos:
        arquivo_podutos.write(texto)



salvar_produto("Celular", "Tira foto", "1500", "celular.jpg")
salvar_produto("Tablet", "Tira foto maior", "2500", "tablet.jpg")
print(obter_produtos())

#3 tipos de abertura de arquivo: "r" (readable), "w" (writable),                   "a" (append)
#                                         |               |                              |
#                                 apenas leitura  escrita, substitui tudo        adiciona linhas


