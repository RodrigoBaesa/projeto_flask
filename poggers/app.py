from flask import Flask, render_template, request, redirect, url_for

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

@app.route("/gerador")
def gerador():
    return render_template("gerador.html")

app.run(port=5001)