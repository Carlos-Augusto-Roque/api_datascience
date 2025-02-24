from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

# Inicializando o aplicativo Flask
app = Flask('projeto')

# Configuração do banco de dados
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Corrigido para False
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')

# Inicializando o SQLAlchemy
mybd = SQLAlchemy(app)

# Modelo da tabela 'Valor'
class Emissao(mybd.Model):
    __tablename__ = 'coleta_residuos'
    id = mybd.Column(mybd.Integer, primary_key=True)
    ano_coleta = mybd.Column(mybd.String(100))
    populacao = mybd.Column(mybd.String(50))
    qtd_residuos_coletados = mybd.Column(mybd.String(100))
    percentual_coleta_seletiva = mybd.Column(mybd.String(50))
    destinacao_principal = mybd.Column(mybd.String(100))
    emissao_co2 = mybd.Column(mybd.String(50))    
    tipo_residuo = mybd.Column(mybd.String(100))  # Incluído no método to_json

    def to_json(self):
        return {"id": self.id, "ano_coleta": self.ano_coleta, "populacao": self.populacao, "qtd_residuos_coletados": self.qtd_residuos_coletados, "percentual_coleta_seletiva": self.percentual_coleta_seletiva, "destinacao_principal": self.destinacao_principal, "emissao_co2": self.emissao_co2, "tipo_residuo": self.tipo_residuo}

@app.route('/')
def index():
    return "<h1>Ola mundo</h1>"
# Rota para obter todos os valores

@app.route("/dados", methods=["GET"])
def seleciona_valor():
    valor_objetos = Emissao.query.all()
    valor_json = [valor.to_json() for valor in valor_objetos]

    return jsonify({"status": 200, "valores": valor_json})

# Executando o aplicativo
if __name__ == "__main__":
    app.run(port=5000, host='127.0.0.1', debug=True)  # Alterado host para 127.0.0.1
