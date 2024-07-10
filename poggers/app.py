from flask import Flask, render_template, request, redirect, url_for
from validate_docbr import CNPJ, CPF

def adicionar_produto(p):
    linha = f"\n{p['nome']},{p['descricao']},{p['preco']},{p['imagem']}"
    with open("produtos.csv", "a") as file:
        file.write(linha)

def obter_produtos():
    with open("produtos.csv", "r") as file:
        lista_produtos= []
        for linha in file:
            nome, descricao, preco, imagem = linha.strip().split(",")
            produto = {
                "nome": nome,
                "descricao": descricao,
                "preco": float(preco),
                "imagem": imagem
            }
            lista_produtos.append(produto)

        return lista_produtos

def gerar_cnpj():
    cnpj = CNPJ()
    new_cnpj = cnpj.generate(True)
    return new_cnpj

def gerar_cpf():
    cpf = CPF()
    new_cpf = cpf.generate(True)
    return new_cpf

def validar_cnpj(cnpj):
    cnpj_validador = CNPJ()
    return cnpj_validador.validate(cnpj)

def validar_cpf(cpf):
    cpf_validador = CPF()
    return cpf_validador.validate(cpf)

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Home</h1>"

@app.route("/contato")
def contato():
    return "<h1>Contato</h1>"

@app.route("/produtos")
def produtos():
    return render_template('produtos.html', produtos=obter_produtos())

@app.route("/produtos/<nome>")
def produto(nome):
    for produto in obter_produtos():
        if produto["nome"].lower() == nome.lower():
            return render_template("produto.html", produto=obter_produtos())
    return "produto não encontrado"

# GET
@app.route("/produtos/cadastro")
def cadastro_produto():
    return render_template("cadastro-produto.html")

# POST
@app.route("/produtos", methods=['POST'])
def salvar_produto():
    nome = request.form['nome']
    descricao = request.form['descricao']
    preco = request.form['preco']
    imagem = request.form['imagem']
    produto = {"nome": nome, "descricao": descricao, "preco": preco, "imagem": imagem}
    adicionar_produto(produto)
    return redirect(url_for("produtos"))

@app.route("/geradorcnpj")
def gerador_cnpj():
    new_cnpj = gerar_cnpj()
    return render_template("geradorcnpj.html", new_cnpj=new_cnpj)

@app.route("/geradorcpf")
def gerador_cpf():
    new_cpf = gerar_cpf()
    return render_template("geradorcpf.html", new_cpf=new_cpf)

# CNPJ
# GET
@app.route("/validarcnpj")
def validar_cnpj_form():
    return render_template("validarcnpj.html")

# POST
@app.route("/validarcnpj", methods=['POST'])
def retorno_cnpj():
    cnpj = request.form['cnpj']
    is_valid = validar_cnpj(cnpj)
    return render_template("retorno_cnpj.html", is_valid=is_valid, cnpj=cnpj)

# CPF
# GET
@app.route("/validarcpf")
def validar_cpf_form():
    return render_template("validarcpf.html")

# POST
@app.route("/validarcpf", methods=['POST'])
def retorno_cpf():
    cpf = request.form['cpf']
    is_valid = validar_cpf(cpf)
    return render_template("retorno_cpf.html", is_valid=is_valid, cpf=cpf)

app.run(port=5001)