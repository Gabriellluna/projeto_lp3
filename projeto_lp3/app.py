from flask import Flask
from validate_docbr import CPF
from validate_docbr import CNPJ

cnpj = CNPJ()
cpf = CPF()
app = Flask("Minha App")

# Uma página do flask é igual a: rota + função
 
#/ home page - Home 
@app.route("/")

def home():
    return "<h1> Home Page!!! </h1>"

#/ contato - página de contato
@app.route("/contato")

def contato():
    return "<h1> Contato </h1>"

#/produtos - pagina produtos
@app.route("/produto")

def produto():
    return "<h1> Produtos Legais </h1>"

#/produtos - pagina servicos
@app.route("/servicos")

def servicos():
    return "<h1> Nossos serviços são: Emissão de notas fiscais, abertura de empresa e fechamento de empresa  </h1>"

#/produtos - pagina gerar-cpf
@app.route("/gerar-cpf")

def gerarcpf():
    cpfs = []
    for i in range(10):
        cpfs.append(cpf.generate(True))
        
    return  f'Aki: {cpfs} '
#/produtos - pagina gerar-cnpj
@app.route("/gerar-cnpj")

def gerarcnpj():
    cnpjs = []

    for i in range(10):
        cnpjs.append(cpf.generate(True))
        
    return  f'Aki: {cnpjs} '
    

#pagina/ servicos retornar "Nosso serviços"
#pagina/ gerar-cpf retornar cpf aleatorio
#pagina/ gerar-cnpj retornar cnpj aleatorio





app.run(debug=True)