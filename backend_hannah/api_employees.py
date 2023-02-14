from flask import Flask, jsonify

app = Flask(__name__)

employees = [
    {
        "id": 1, 
        "prenom": "Hannah", 
        "nom": "DELATTRE", 
        "adresse": "1 Rue des Pistaches", 
        "email": "hannah.delattre@gmail.com"
    },
    {
        "id": 2, 
        "prenom": "Leny", 
        "nom": "ROUSSEAU", 
        "adresse": "2 Rue des Tagadas", 
        "email": "leny.rousseau@gmail.com"
    },
    {
        "id": 3, 
        "prenom": "Pierre", 
        "nom": "Durand", 
        "adresse": "3 Rue des Champs", 
        "email": "pierre.durand@hotmail.com"
        },
    {
        "id": 4, 
        "prenom": "Alice", 
        "nom": "Dubois", 
        "adresse": "1 Rue de la Paix", 
        "email": "alice.dubois@gmail.com"}
]

@app.route('/hannah')
def get_hello_world():
    return '<div style="text-align:center"><h1>Hello World!</h1></div>'

@app.route('/api/v1')
def get_employees():
    return jsonify(employees)

if __name__ == '__main__':
    app.run(port=8080)