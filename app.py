import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

# Inicializando o aplicativo Flask
app = Flask('projeto')

# Corrigindo a string de conexão com URL codificada
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://admindatabase:senai%23134@senaiserverdatabase.mysql.database.azure.com:3306/projetointegrador"

# Configuração do banco de dados com SSL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

# Inicializando o SQLAlchemy
db = SQLAlchemy(app)

# Modelo da tabela 'coleta_residuos'
class Emissao(db.Model):
    __tablename__ = 'coleta_residuos'
    id = db.Column(db.Integer, primary_key=True)
    ano_coleta = db.Column(db.String(100))
    populacao = db.Column(db.String(50))
    qtd_residuos_coletados = db.Column(db.String(100))
    percentual_coleta_seletiva = db.Column(db.String(50))
    destinacao_principal = db.Column(db.String(100))
    emissao_co2 = db.Column(db.String(50))    
    tipo_residuo = db.Column(db.String(100))

    def to_json(self):
        return {
            "id": self.id,
            "ano_coleta": self.ano_coleta,
            "populacao": self.populacao,
            "qtd_residuos_coletados": self.qtd_residuos_coletados,
            "percentual_coleta_seletiva": self.percentual_coleta_seletiva,
            "destinacao_principal": self.destinacao_principal,
            "emissao_co2": self.emissao_co2,
            "tipo_residuo": self.tipo_residuo,
        }

@app.route('/')
def index():
    return "<h1>Olá, mundo!</h1>"

@app.route("/dados", methods=["GET"])
def seleciona_valor():
    valor_objetos = Emissao.query.all()
    valor_json = [valor.to_json() for valor in valor_objetos]
    return jsonify({"status": 200, "valores": valor_json})

# Executando o aplicativo
if __name__ == "__main__":
    app.run(port=5000, host='127.0.0.1', debug=True)
