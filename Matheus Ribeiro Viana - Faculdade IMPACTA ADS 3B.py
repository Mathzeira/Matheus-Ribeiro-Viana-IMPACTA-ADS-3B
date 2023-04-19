from flask import Flask,jsonify

app = Flask(__name__)

marcas = [
        {'id': 1, 'marcas': 'Uber'},
        {'id': 2, 'marcas': 'Xbox'},
        {'id': 3, 'marcas': 'Samsung'},     
    ]

@app.route('/marcas', methods=['GET'])
def buscar():  
    return jsonify(marcas,)

if __name__ == '__main__':
    app.run(debug=True, port=505)
