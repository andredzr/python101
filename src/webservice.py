from flask import Flask, jsonify
import csv

app = Flask(__name__)

@app.route('/', methods=['GET'])
def csv_a_json():
    with open('data/employees.csv', 'r') as archivo_csv:
        lector_dict = csv.DictReader(archivo_csv)
        lista = []
        for linea in lector_dict:
            lista.append(linea)
        return jsonify(lista)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")