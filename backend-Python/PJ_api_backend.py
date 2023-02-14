from flask import Flask, jsonify, request

app = Flask(__name__)

employees = [
    {'id': 1, 'firstName': 'John', 'lastName': 'Doe', 'emailId': 'johndoe@example.com'},
    {'id': 2, 'firstName': 'Jane', 'lastName': 'Smith', 'emailId': 'janesmith@example.com'},
    {'id': 3, 'firstName': 'Bob', 'lastName': 'Johnson', 'emailId': 'bobjohnson@example.com'}
]

@app.route('/api/v1/employees', methods=['GET'])
def get_employees():
    return jsonify(employees)

@app.route('/api/v1/employees', methods=['POST'])
def add_employee():
    new_employee = request.json
    new_employee['id'] = len(employees) + 1
    employees.append(new_employee)
    return jsonify(new_employee), 201

@app.route('/api/v1/<int:id>', methods=['PUT'])
def update_employee(id):
    for employee in employees:
        if employee['id'] == id:
            employee['firstName'] = request.json['firstName']
            employee['lastName'] = request.json['lastName']
            employee['emailId'] = request.json['emailId']
            return jsonify(employee)
    return jsonify({'result': False, 'message': 'Employee not found'})

if __name__ == '__main__':
    app.run(debug=True, port=8080)