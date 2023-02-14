from flask import Flask, jsonify, request

app = Flask(__name__)

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

@app.route('/api/v1', methods=['POST'])
def add_employee():
    new_employee = request.get_json()
    employees.append(new_employee)
    return jsonify(new_employee)

@app.route('/api/v1/<int:id>', methods=['DELETE'])
def delete_employee(id):
    for employee in employees:
        if employee['id'] == id:
            employees.remove(employee)
            return jsonify({'result': True})
    return jsonify({'result': False, 'message': 'Employee not found'})

@app.route('/api/v1', methods=['GET'])
def get_employees():
    return jsonify(employees)

if __name__ == '__main__':
    app.run(port=8080)