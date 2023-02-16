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

@app.route('/api/v1/employees/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    for employee in employees:
        if employee['id'] == employee_id:
            employees.remove(employee)
            return jsonify({'message': 'Employee has been deleted'}), 200
    return jsonify({'error': 'Employee not found'}), 404

@app.route('/api/v1/employees/<int:employee_id>', methods=['PUT'])
def update_employee(employee_id):
    for employee in employees:
        if employee['id'] == employee_id:
            employee.update(request.json)
            return jsonify(employee), 200
    return jsonify({'error': 'Employee not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, port=8080)