from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

products = [
    {
        'id': 1,
        'title': 'Product 1',
        'description': 'This is the first product',
        'price': 9.99,
        'image': 'https://example.com/product1.jpg'
    },
    {
        'id': 2,
        'title': 'Product 2',
        'description': 'This is the second product',
        'price': 19.99,
        'image': 'https://example.com/product2.jpg'
    },
    {
        'id': 3,
        'title': 'Product 3',
        'description': 'This is the third product',
        'price': 29.99,
        'image': 'https://example.com/product3.jpg'
    }
]

@app.route('/products', methods=['GET', 'POST'])
def manage_products():
    if request.method == 'GET':
        return jsonify({'products': products})

    if request.method == 'POST':
        product = {
            'id': products[-1]['id'] + 1,
            'title': request.json['title'],
            'description': request.json['description'],
            'price': request.json['price'],
            'image': request.json['image']
        }
        products.append(product)
        return jsonify({'product': product}), 201

@app.route('/product/<int:product_id>', methods=['GET', 'DELETE'])
def manage_product(product_id):
    product = [product for product in products if product['id'] == product_id]
    if len(product) == 0:
        return jsonify({'error': 'Product not found here'})

    if request.method == 'GET':
        return jsonify({'product': product[0]})

    if request.method == 'DELETE':
        products.remove(product[0])
        return jsonify({'result': 'Product deleted'})

employees = [
    {
        "id": 1, 
        "firstName": "Hannah", 
        "lastName": "DELATTRE", 
        "emailId": "hannah.delattre@gmail.com"
    },
    {
        "id": 2, 
        "firstName": "Leny", 
        "lastName": "ROUSSEAU", 
        "emailId": "leny.rousseau@gmail.com"
    },
    {
        "id": 3, 
        "firstName": "Pierre", 
        "lastName": "Durand", 
        "emailId": "pierre.durand@hotmail.com"
    },
    {
        "id": 4, 
        "firstName": "Alice", 
        "lastName": "Dubois", 
        "emailId": "alice.dubois@gmail.com"}
]

@app.route('/hannah')
def get_hello_world():
    return '<div style="text-align:center"><h1>Hello World!</h1></div>'

@app.route('/api/v1/employees/', methods=['POST'])
def add_employee():
    new_employee = request.get_json()
    employees.append(new_employee)
    return jsonify(new_employee)

@app.route('/api/v1/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    for employee in employees:
        if employee['id'] == id:
            employees.remove(employee)
            return jsonify({'result': True})
    return jsonify({'result': False, 'message': 'Employée non trouvé'})

@app.route('/api/v1/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    for employee in employees:
        if employee['id'] == id:
            employee['firstName'] = request.json['firstName']
            employee['lastName'] = request.json['lastName']
            employee['emailId'] = request.json['emailId']
            return jsonify(employee)
    return jsonify({'result': False, 'message': 'Employee non trouvé'})

@app.route('/api/v1/employees/', methods=['GET'])
def get_employees():
    return jsonify(employees)

if __name__ == '__main__':
    app.run(debug=True)