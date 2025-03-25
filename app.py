from flask import Flask, jsonify
import random

app = Flask(__name__)

charadas = [
    {"id": 1, "charada": "O que é, o que é? A capital brasileira que está presente em todos os aniversários.", "resposta": "Palmas"},
    {"id": 2, "charada": "O que é, o que é? A diferença entre a bota e a calça.", "resposta": "A bota, a gente calça, e a calça, a gente bota."},
    {"id": 3, "charada": "O que é, o que é? Que dá o poder de atravessar paredes.", "resposta": "A porta."},
    {"id": 4, "charada": "O que é, o que é? Tem centenas de rodas, mas não sai do lugar.", "resposta": "O estacionamento."},
    {"id": 5, "charada": "O que é, o que é? Uma impressora disse para a outra.", "resposta": "Essa folha é sua ou é impressão minha?"},
    {"id": 6, "charada": "O que é, o que é? É proibido comer no café da manhã.", "resposta": "O almoço e o jantar."},
    {"id": 7, "charada": "O que é, o que é? O zero disse para o oito.", "resposta": "Belo cinto."},
    {"id": 8, "charada": "O que é, o que é? O motivo dos ovos não contarem piadas.", "resposta": "Para não rachar de rir."},
    {"id": 9, "charada": "O que é, o que é? A praia disse ao mar.", "resposta": "Deixa de onda."},
    {"id": 10, "charada": "O que é, o que é? Quebra quando se fala.", "resposta": "O segredo."},
    {"id": 11, "charada": "O que é, o que é? No início muda e no fim dança.", "resposta": "A mudança."},
    {"id": 12, "charada": "O que é, o que é? Faz parte das árvores e dos cadernos.", "resposta": "As folhas."},
    {"id": 13, "charada": "O que é, o que é? Um ponteiro disse para o outro.", "resposta": "Encontro você ao meio dia."},
    {"id": 14, "charada": "O que é, o que é? Tem apenas duas letras, é redondo e tem um buraco no meio.", "resposta": "O CD."},
    {"id": 15, "charada": "O que é, o que é? Tem cinco dedos, mas não tem unhas.", "resposta": "A luva."},
    {"id": 16, "charada": "O que é, o que é? Está no final do arco-íris.", "resposta": "A letra S."},
    {"id": 17, "charada": "O que é, o que é? A formiga tem maior que o leão.", "resposta": "O nome."},
    {"id": 18, "charada": "O que é, o que é? Cru não existe e cozido não se come.", "resposta": "O sabão em barra."},
    {"id": 19, "charada": "O que é, o que é? Tem dentes, mas nunca come.", "resposta": "O garfo."},
    {"id": 20, "charada": "O que é, o que é? Corre, mas não tem pés.", "resposta": "O vento."}
]

@app.route('/')
def index():
    return ('index.html')

@app.route('/charadas', methods=['GET'])
def listacharadas():
    return jsonify(charadas), 200

@app.route('/charadas/aleatoria', methods=['GET'])
def charada_aleatoria():
    #função que gera a charada aleatoria
    charadaaleatoria = random.choice(charadas)
    return jsonify(charadaaleatoria), 200

@app.route('/charadas/<campo>/<busca>', methods=['GET'])
def buscar(campo, busca):
    if campo not in ['id', 'charada']:
        return jsonify({'mensagem': 'ERRO'}), 400
    
    if campo == 'id':
        busca = int(busca)

    for charada in charadas:
        if charada[campo] == busca:
            return jsonify(charada), 200
    
    return jsonify({'mensagem': 'Charada não encontrada'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
