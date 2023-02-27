from flask import Flask, request, jsonify

app = Flask(__name__)

products = [
]

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
