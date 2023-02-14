from flask import Flask

app = Flask(__name__)

data = [
    {"id": 1, "prenom": "Hannah", "nom": "DELATTRE", "adresse": "1 Rue des Pistaches", "email": "hannah.delattre@gmail.com"},
    {"id": 2, "prenom": "Leny", "nom": "ROUSSEAU", "adresse": "2 Rue des Tagadas", "email": "leny.rousseau@gmail.com"},
    {"id": 3, "prenom": "Pierre", "nom": "Durand", "adresse": "3 Rue des Champs", "email": "pierre.durand@hotmail.com"},
    {"prenom": "Alice", "nom": "Dubois", "adresse": "1 Rue de la Paix, Paris", "email": "alice.dubois@gmail.com"}
]

@app.route('/hannah')
def hello_world():
    return '<div style="text-align:center"><h1>Hello World!</h1></div>'

if __name__ == '__main__':
    app.run(port=8081)