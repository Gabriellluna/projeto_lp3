from flask import Flask, render_template
from validate_docbr import CPF
from validate_docbr import CNPJ


cnpj = CNPJ()
cpf = CPF()
app = Flask("Minha App")

# Uma página do flask é igual a: rota + função
 
#/ home page - Home 
@app.route("/")

def home():
    return render_template("home.html")

#/ contato - página de contato
@app.route("/contato")

def contato():
    return render_template("contato.html")

#/produtos - pagina produtos
@app.route("/produto")

def produtos():
    lista_produtos = [
        {"nome" : "Coca-Cola", "descricao" : "Mata a sede"},
        {"nome" : "Doritos", "descricao" : "Suja a mão"},
        {"nome" : "Chocolate", "descricao" : "Bom"},
    ]
    return render_template("produto.html", produtos = lista_produtos)

#/produtos - pagina servicos
@app.route("/servicos")

def servicos():
    return render_template("servicos.html")

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