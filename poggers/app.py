from flask import Flask, render_template

lista_produtos = [
    {"nome": "Coca-Cola", "descricao": "Refrigerante popular e refrescante, conhecido por seu sabor único e por ser uma opção clássica em eventos e refeições."},
    {"nome": "Trembo", "descricao": "Suplemento para crescimento muscular, muito utilizado por atletas e fisiculturistas para maximizar os ganhos de força e massa muscular."},
    {"nome": "Camarão", "descricao": "Fruto do mar versátil e saboroso, pode ser preparado de diversas formas, mas algumas pessoas podem não gostar do seu sabor ou textura."},
    {"nome": "Mac and Cheese", "descricao": "Prato clássico americano feito de macarrão e queijo, apreciado por seu sabor cremoso e reconfortante, ideal para todas as idades."},
    {"nome": "iPhone", "descricao": "Smartphone de alta tecnologia da Apple, conhecido por sua interface intuitiva, câmera de qualidade e um vasto ecossistema de aplicativos."},
    {"nome": "Nike Air Max", "descricao": "Tênis esportivo famoso pelo seu conforto e design inovador, utilizado tanto para atividades físicas quanto para uso casual."},
    {"nome": "Livro 'O Senhor dos Anéis'", "descricao": "Clássico da literatura de fantasia escrito por J.R.R. Tolkien, apresenta uma épica aventura na Terra Média com personagens memoráveis."},
    {"nome": "Smart TV Samsung", "descricao": "Televisor inteligente com resolução 4K, oferece uma experiência de visualização imersiva e acesso a diversos aplicativos de streaming."},
    {"nome": "Pizza Margherita", "descricao": "Pizza clássica italiana feita com molho de tomate, mussarela e manjericão fresco, apreciada por seu sabor autêntico e simples."},
    {"nome": "Bicicleta Mountain Bike", "descricao": "Bicicleta robusta e versátil, projetada para trilhas e terrenos acidentados, proporcionando uma experiência de ciclismo emocionante e desafiadora."},
    {"nome": "PlayStation 5", "descricao": "Console de videogame de última geração da Sony, oferece gráficos impressionantes e uma vasta biblioteca de jogos exclusivos."},
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
            return render_template('descricao.html', produto=produto)
            # return f"{produto['nome']}, {produto['descricao'] }"
    
    return "Produto não encontrado"