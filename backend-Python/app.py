from flask import Flask, request, jsonify

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)