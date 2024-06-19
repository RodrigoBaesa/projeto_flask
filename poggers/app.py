from flask import Flask, render_template, request, redirect, url_for

lista_produtos = [
    {"nome": "Coca-Cola", "descricao": "Refrigerante popular e refrescante, conhecido por seu sabor único e por ser uma opção clássica em eventos e refeições.", "preco": 40, "imagem": "https://sm.ign.com/ign_br/cover/d/dark-and-d/dark-and-darker_txee.jpg"},
    {"nome": "Camarão", "descricao": "Fruto do mar versátil e saboroso, pode ser preparado de diversas formas, mas algumas pessoas podem não gostar do seu sabor ou textura.", "preco": 40, "imagem": "https://cdn-icons-png.flaticon.com/512/4436/4436481.png"},
    {"nome": "Mac and Cheese", "descricao": "Prato clássico americano feito de macarrão e queijo, apreciado por seu sabor cremoso e reconfortante, ideal para todas as idades.", "preco": 40, "imagem": "https://cdn-icons-png.flaticon.com/512/4436/4436481.png"},
    {"nome": "iPhone", "descricao": "Smartphone de alta tecnologia da Apple, conhecido por sua interface intuitiva, câmera de qualidade e um vasto ecossistema de aplicativos.", "preco": 40, "imagem": "https://cdn-icons-png.flaticon.com/512/4436/4436481.png"},
    {"nome": "Nike Air Max", "descricao": "Tênis esportivo famoso pelo seu conforto e design inovador, utilizado tanto para atividades físicas quanto para uso casual.", "preco": 40, "imagem": "https://cdn-icons-png.flaticon.com/512/4436/4436481.png"},
]

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Home</h1>"

@app.route("/contato")
def contato():
    return "<h1>Contato</h1>"

@app.route("/produtos")
def produtos():
    return render_template('produtos.html', produtos=lista_produtos)

@app.route("/produtos/<nome>")
def produto(nome):
    for produto in lista_produtos:
        if produto["nome"].lower() == nome.lower():
            return render_template("produto.html", produto=produto)
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
    lista_produtos.append(produto)

    return redirect(url_for("produtos"))

app.run(port=5001)